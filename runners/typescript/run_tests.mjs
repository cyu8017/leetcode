#!/usr/bin/env node
/** TypeScript test runner: validates via transpiled JS when possible. */

import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { preRunCheck, EXIT } from "../common/runner_policy.mjs";

const problemDir = path.resolve(process.argv[2]);
const repoRoot = path.resolve(path.dirname(new URL(import.meta.url).pathname), "../..");
const jsRunner = path.join(repoRoot, "runners", "javascript", "run_tests.mjs");

if (!problemDir) {
  console.error("Usage: run_tests.mjs <problem_dir>");
  process.exit(2);
}

console.log(`TypeScript tests: ${path.basename(problemDir)}`);
const tsFile = path.join(problemDir, "solution.ts");
if (!fs.existsSync(tsFile)) {
  console.log("  missing solution.ts");
  process.exit(EXIT.CONFIG);
}

const config = JSON.parse(fs.readFileSync(path.join(problemDir, "tests", "config.json"), "utf8").replace(/^\uFEFF/, ""));
const casesDoc = JSON.parse(fs.readFileSync(path.join(problemDir, "tests", "cases.json"), "utf8").replace(/^\uFEFF/, ""));
const check = preRunCheck("typescript", config, casesDoc, {
  hasSolutionFile: true,
});
if (!check.canRun) {
  console.log(`  ${check.message}`);
  process.exit(check.exitCode);
}

const tsc = spawnSync("npx", ["--yes", "--package", "typescript", "tsc", "--target", "ES2020", "--module", "CommonJS", "--outDir", path.join(problemDir, ".test-build"), tsFile], {
  cwd: problemDir,
  shell: true,
  stdio: "inherit",
});

if (tsc.status !== 0) {
  console.log("  unable to transpile solution.ts");
  process.exit(EXIT.CONFIG);
}

const builtJs = path.join(problemDir, ".test-build", "solution.js");
if (!fs.existsSync(builtJs)) {
  console.log("  transpile output not found");
  process.exit(EXIT.CONFIG);
}

const tempJs = path.join(problemDir, "solution.js");
const backupExists = fs.existsSync(tempJs);
const backup = backupExists ? fs.readFileSync(tempJs) : null;
fs.copyFileSync(builtJs, tempJs);

const result = spawnSync(process.execPath, [jsRunner, problemDir], { stdio: "inherit" });

if (backupExists && backup) {
  fs.writeFileSync(tempJs, backup);
} else if (!backupExists) {
  fs.unlinkSync(tempJs);
}

process.exit(result.status ?? 1);
