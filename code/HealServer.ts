#!/usr/bin/env node

import { htmlEscaped, runCommand } from "./utils"
import { jtree } from "jtree"

const path = require("path")
const fs = require("fs")
const https = require("https")
const express = require("express")
const bodyParser = require("body-parser")
const numeral = require("numeral")
const { Disk } = require("jtree/products/Disk.node.js")
const { TreeNode } = jtree
const { TreeBaseFolder } = require("jtree/products/treeBase.node.js")
const { ScrollFile, getFullyExpandedFile } = require("scroll-cli")

const baseFolder = path.join(__dirname, "..")
const databaseFolder = path.join(baseFolder, "database")
const ignoreFolder = path.join(baseFolder, "ignore")
const builtSiteFolder = path.join(baseFolder, "site")

const base = new TreeBaseFolder()
	.setDir(path.join(databaseFolder, "things"))
	.setGrammarDir(path.join(databaseFolder, "grammar"))
	.loadFolder()

const searchLogPath = path.join(ignoreFolder, "searchLog.tree")
Disk.touch(searchLogPath)

const scrollSettings = getFullyExpandedFile(
	path.join(builtSiteFolder, "settings.scroll")
).code

class HealServer {
	homepage = this.scrollToHtml(`
 `)

	app = undefined
	constructor() {
		const app = express()
		this.app = app
		app.use(bodyParser.urlencoded({ extended: false }))
		app.use(bodyParser.json())
		app.use((req: any, res: any, next: any) => {
			res.setHeader("Access-Control-Allow-Origin", "*")
			res.setHeader(
				"Access-Control-Allow-Methods",
				"GET, POST, OPTIONS, PUT, PATCH, DELETE"
			)
			res.setHeader(
				"Access-Control-Allow-Headers",
				"X-Requested-With,content-type"
			)
			res.setHeader("Access-Control-Allow-Credentials", true)
			next()
		})

		app.get("/", (req: any, res: any) => res.send(this.homepage))

		app.use(express.static(__dirname))
		app.use(express.static(builtSiteFolder))

		const searchCache = {}

		app.get("/search", (req, res) => {
			const originalQuery = req.query.q ?? ""
			const tree = `search
 time ${Date.now()}
 ip ${req.ip}
 query
  ${originalQuery.replace(/\n/g, "\n  ")}
`
			fs.appendFile(searchLogPath, tree, function() {})

			if (searchCache[originalQuery]) {
				res.send(searchCache[originalQuery])
				return
			}
			searchCache[originalQuery] = this.scrollToHtml(
				this.search(decodeURIComponent(originalQuery))
			)

			res.send(searchCache[originalQuery])
		})
	}

	search(query): string {
		const startTime = Date.now()
		// Todo: allow advanced search. case sensitive/insensitive, regex, et cetera.
		const testFn = str => str?.includes(query)

		const escapedQuery = htmlEscaped(query)
		const hits = base.filter(file => testFn(file.toString()))
		const nameHits = [] // base.filter(file => file.lowercaseNames.some(testFn))
		const baseUrl = "https://newtondb.com/treatments/"

		const highlightHit = file => {
			const line = file
				.toString()
				.split("\n")
				.find(line => testFn(line))
			return line.replace(query, `<span style="highlightHit">${query}</span>`)
		}
		const fullTextSearchResults = hits
			.map(
				file =>
					` <div class="searchResultFullText"><a href="${baseUrl}${
						file.permalink
					}">${file.title}</a> - ${file.get("type")} #${
						file.rank
					} - ${highlightHit(file)}</div>`
			)
			.join("\n")

		const nameResults = nameHits
			.map(
				file =>
					` <div class="searchResultName"><a href="${baseUrl}${
						file.permalink
					}">${file.title}</a> - ${file.get("type")} #${file.rank}</div>`
			)
			.join("\n")

		const time = numeral((Date.now() - startTime) / 1000).format("0.00")
		return `
html
 <div class="pldbSearchForm"><form style="display:inline;" method="get" action="https://heal.newtondb.com/search"><input name="q" placeholder="Search" autocomplete="off" type="search" id="searchFormInput"><input class="pldbSearchButton" type="submit" value="Search"></form></div>
 <script>document.addEventListener("DOMContentLoaded", evt => initSearchAutocomplete("searchFormInput"))</script>

* <p class="searchResultsHeader">Searched ${numeral(0).format(
			"0,0"
		)} treatments and entities for "${escapedQuery}" in ${time}s.</p><hr>

html
 <p class="searchResultsHeader">Showing ${
		nameHits.length
 } files whose name or aliases matched.</p>

html
${nameResults}
<hr>

* <p class="searchResultsHeader">Showing ${
			hits.length
		} files who matched on a full text search.</p>

html
 ${fullTextSearchResults}`
	}

	listen(port = 4444) {
		this.app.listen(port, () =>
			console.log(
				`HealServer server running: \ncmd+dblclick: http://localhost:${port}/`
			)
		)
		return this
	}

	scrollToHtml(scrollContent) {
		return new ScrollFile(
			`replace BASE_URL ${this.isProd ? "https://newtondb.com" : ""}
replace BUILD_URL ${this.isProd ? "https://heal.newtondb.com" : "/"}

${scrollSettings}
maxColumns 1
columnWidth 200

css
 #editForm {
  width: 100%;
  height: 80%;
 }
 .cell {
   width: 48%;
   display: inline-block;
   vertical-align: top;
   padding: 5px;
 }
 #quickLinks, .missingRecommendedColumns {
   font-size: 80%;
 }


html
 <div id="successLink"></div>
 <div id="errorMessage" style="color: red;"></div>

${scrollContent}
`
		).html
	}

	isProd = false

	listenProd() {
		this.isProd = true
		const key = fs.readFileSync(path.join(ignoreFolder, "privkey.pem"))
		const cert = fs.readFileSync(path.join(ignoreFolder, "fullchain.pem"))
		https
			.createServer(
				{
					key,
					cert
				},
				this.app
			)
			.listen(443)

		const redirectApp = express()
		redirectApp.use((req, res) =>
			res.redirect(301, `https://${req.headers.host}${req.url}`)
		)
		redirectApp.listen(80, () => console.log(`Running redirect app`))
		return this
	}
}

class HealServerCommands {
	startDevServerCommand(port) {
		new HealServer().listen(port)
	}

	startProdServerCommand() {
		new HealServer().listenProd()
	}
}

export { HealServer }

if (!module.parent)
	runCommand(new HealServerCommands(), process.argv[2], process.argv[3])
