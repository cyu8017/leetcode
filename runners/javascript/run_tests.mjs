#!/usr/bin/env node
/** Run tests for a LeetCode JavaScript solution. */

import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { runDesignCases, usesDesignCases } from "./design_tests.mjs";
import { preRunCheck, EXIT } from "../common/runner_policy.mjs";

function listToListNode(values) {
  if (!values || values.length === 0) return null;
  const head = { val: values[0], next: null };
  let current = head;
  for (let i = 1; i < values.length; i += 1) {
    current.next = { val: values[i], next: null };
    current = current.next;
  }
  return head;
}

function listToCycleList(values, pos = -1) {
  if (!values || values.length === 0) return null;
  const nodes = values.map((value) => ({ val: value, next: null }));
  for (let i = 0; i < nodes.length - 1; i += 1) {
    nodes[i].next = nodes[i + 1];
  }
  if (pos >= 0 && pos < nodes.length) {
    nodes[nodes.length - 1].next = nodes[pos];
  }
  return nodes[0];
}

function listNodeToList(node) {
  const result = [];
  const seen = new Set();
  while (node && !seen.has(node)) {
    seen.add(node);
    result.push(node.val);
    node = node.next;
  }
  return result;
}

function cycleEntryToString(node, head) {
  if (!node) return "no cycle";
  let index = 0;
  let current = head;
  const seen = new Set();
  while (current && !seen.has(current)) {
    if (current === node) return `tail connects to node index ${index}`;
    seen.add(current);
    current = current.next;
    index += 1;
  }
  return "no cycle";
}

function buildIntersectionLists(args) {
  const listA = args.listA || [];
  const listB = args.listB || [];
  const skipA = args.skipA ?? 0;
  const skipB = args.skipB ?? 0;
  const intersectVal = args.intersectVal ?? 0;

  const nodesA = listA.map((value) => ({ val: value, next: null }));
  for (let i = 0; i < nodesA.length - 1; i += 1) nodesA[i].next = nodesA[i + 1];

  if (!intersectVal || skipA >= nodesA.length) {
    const nodesB = listB.map((value) => ({ val: value, next: null }));
    for (let i = 0; i < nodesB.length - 1; i += 1) nodesB[i].next = nodesB[i + 1];
    return [nodesA[0] || null, nodesB[0] || null];
  }

  const nodesB = listB.slice(0, skipB).map((value) => ({ val: value, next: null }));
  for (let i = 0; i < nodesB.length - 1; i += 1) nodesB[i].next = nodesB[i + 1];
  if (nodesB.length > 0) nodesB[nodesB.length - 1].next = nodesA[skipA];
  return [nodesA[0] || null, nodesB[0] || nodesA[skipA] || null];
}

function intersectNodeToString(node) {
  if (!node) return "No intersection";
  return `Intersected at '${node.val}'`;
}

function isWiggle(nums) {
  for (let index = 0; index < nums.length - 1; index += 1) {
    if (index % 2 === 0) {
      if (nums[index] >= nums[index + 1]) return false;
    } else if (nums[index] <= nums[index + 1]) {
      return false;
    }
  }
  return true;
}

function findTreeNode(root, val) {
  if (!root) return null;
  if (root.val === val) return root;
  return findTreeNode(root.left, val) || findTreeNode(root.right, val);
}

function findListNode(head, val) {
  while (head) {
    if (head.val === val) return head;
    head = head.next;
  }
  return null;
}

function listToTree(values) {
  if (!values || values.length === 0) return null;
  const root = { val: values[0], left: null, right: null };
  const queue = [root];
  let i = 1;
  while (queue.length > 0 && i < values.length) {
    const node = queue.shift();
    if (i < values.length) {
      if (values[i] !== null && values[i] !== undefined) {
        node.left = { val: values[i], left: null, right: null };
        queue.push(node.left);
      }
      i += 1;
    }
    if (i < values.length) {
      if (values[i] !== null && values[i] !== undefined) {
        node.right = { val: values[i], left: null, right: null };
        queue.push(node.right);
      }
      i += 1;
    }
  }
  return root;
}

function listToParentTree(values) {
  if (!values || values.length === 0) return null;
  const root = { val: values[0], left: null, right: null, parent: null };
  const queue = [root];
  let i = 1;
  while (queue.length > 0 && i < values.length) {
    const node = queue.shift();
    if (i < values.length) {
      if (values[i] !== null && values[i] !== undefined) {
        node.left = { val: values[i], left: null, right: null, parent: node };
        queue.push(node.left);
      }
      i += 1;
    }
    if (i < values.length) {
      if (values[i] !== null && values[i] !== undefined) {
        node.right = { val: values[i], left: null, right: null, parent: node };
        queue.push(node.right);
      }
      i += 1;
    }
  }
  return root;
}

function findParentNode(root, val) {
  if (!root) return null;
  if (root.val === val) return root;
  const left = findParentNode(root.left, val);
  if (left) return left;
  return findParentNode(root.right, val);
}

function treeToList(root) {
  if (!root) return [];
  const result = [];
  const queue = [root];
  while (queue.length > 0) {
    const node = queue.shift();
    if (!node) {
      result.push(null);
      continue;
    }
    result.push(node.val);
    queue.push(node.left);
    queue.push(node.right);
  }
  while (result.length > 0 && result[result.length - 1] === null) {
    result.pop();
  }
  return result;
}

function listToNextNode(values) {
  if (!values || values.length === 0) return null;
  const root = { val: values[0], left: null, right: null, next: null };
  const queue = [root];
  let i = 1;
  while (queue.length > 0 && i < values.length) {
    const node = queue.shift();
    if (i < values.length) {
      if (values[i] !== null && values[i] !== undefined) {
        node.left = { val: values[i], left: null, right: null, next: null };
        queue.push(node.left);
      }
      i += 1;
    }
    if (i < values.length) {
      if (values[i] !== null && values[i] !== undefined) {
        node.right = { val: values[i], left: null, right: null, next: null };
        queue.push(node.right);
      }
      i += 1;
    }
  }
  return root;
}

function nextNodeToSerialized(root) {
  if (!root) return [];
  const parts = [];
  let level = root;
  while (level) {
    let current = level;
    while (current) {
      parts.push(String(current.val));
      current = current.next;
    }
    parts.push("#");
    current = level;
    let nextLevel = null;
    while (current) {
      if (current.left) {
        nextLevel = current.left;
        break;
      }
      if (current.right) {
        nextLevel = current.right;
        break;
      }
      current = current.next;
    }
    level = nextLevel;
  }
  return `[${parts.join(",")}]`;
}

function listToNary(values) {
  if (!values || values.length === 0) return null;
  const root = { val: values[0], children: [] };
  let parents = [root];
  let index = 1;
  if (index < values.length && values[index] === null) index += 1;

  while (parents.length > 0) {
    const nextParents = [];
    let parentIndex = 0;
    while (index < values.length && values[index] === null) index += 1;
    while (parentIndex < parents.length && index < values.length) {
      const parent = parents[parentIndex];
      const segment = [];
      while (index < values.length && values[index] !== null) {
        segment.push(values[index]);
        index += 1;
      }
      for (const value of segment) {
        const child = { val: value, children: [] };
        parent.children.push(child);
        nextParents.push(child);
      }
      parentIndex += 1;
      if (index < values.length && values[index] === null) {
        index += 1;
        if (index < values.length && values[index] === null) {
          index += 1;
          parentIndex = parents.length;
          break;
        }
      }
    }
    parents = nextParents;
  }
  return root;
}

function naryToList(root) {
  if (!root) return [];
  const result = [root.val];
  let parents = [root];
  while (parents.length > 0) {
    const nextParents = [];
    const segments = parents.map((parent) => parent.children.map((child) => child.val));
    for (const parent of parents) {
      nextParents.push(...parent.children);
    }
    if (nextParents.length === 0) break;
    let padding = 0;
    for (const segment of segments) {
      if (!segment.length) padding += 1;
      else break;
    }
    for (let i = 0; i < padding; i += 1) result.push(null);
    for (let segmentIndex = padding; segmentIndex < segments.length; segmentIndex += 1) {
      const segment = segments[segmentIndex];
      if (segment.length) result.push(...segment);
      if (segmentIndex < segments.length - 1) result.push(null);
    }
    parents = nextParents;
  }
  return result;
}

function naryTreesEqual(left, right) {
  if (!left && !right) return true;
  if (!left || !right) return false;
  if (left.val !== right.val || left.children.length !== right.children.length) return false;
  return left.children.every((child, index) => naryTreesEqual(child, right.children[index]));
}

function quadTreeToList(root) {
  if (!root) return [];
  const result = [];
  const queue = [root];
  while (queue.length > 0) {
    const node = queue.shift();
    if (!node) {
      result.push(null);
      continue;
    }
    result.push([Number(node.isLeaf), Number(node.val)]);
    if (node.isLeaf) {
      queue.push(null, null, null, null);
    } else {
      queue.push(node.topLeft, node.topRight, node.bottomLeft, node.bottomRight);
    }
  }
  while (result.length > 0 && result[result.length - 1] === null) {
    result.pop();
  }
  return result;
}

function splitMultilevelRows(values) {
  const rows = [];
  let index = 0;
  while (index < values.length) {
    const row = [];
    while (index < values.length && values[index] !== null) {
      row.push(index);
      index += 1;
    }
    if (row.length) rows.push(row);
    if (index < values.length && values[index] === null) index += 1;
    while (index < values.length && values[index] === null) index += 1;
  }
  return rows;
}

function listToMultilevel(values) {
  if (!values || values.length === 0) return null;
  const nodes = {};
  values.forEach((value, nodeIndex) => {
    if (value !== null && value !== undefined) {
      nodes[nodeIndex] = { val: value, prev: null, next: null, child: null };
    }
  });
  const rows = splitMultilevelRows(values);
  for (const row of rows) {
    for (let position = 0; position < row.length; position += 1) {
      const node = nodes[row[position]];
      if (position > 0) {
        const previousIndex = row[position - 1];
        node.prev = nodes[previousIndex];
        nodes[previousIndex].next = node;
      }
    }
  }
  for (let rowIndex = 0; rowIndex < rows.length - 1; rowIndex += 1) {
    const parentRow = rows[rowIndex];
    const childRow = rows[rowIndex + 1];
    let padding = childRow[0] - parentRow[parentRow.length - 1] - 2;
    if (padding < 0) padding = 0;
    if (padding < parentRow.length) {
      nodes[parentRow[padding]].child = nodes[childRow[0]];
    }
  }
  return nodes[rows[0][0]];
}

function multilevelToList(head) {
  const result = [];
  let current = head;
  while (current) {
    result.push(current.val);
    current = current.next;
  }
  return result;
}

function doublyTreeNodeToList(head) {
  if (!head) return [];
  const result = [];
  let node = head;
  const start = head;
  while (true) {
    result.push(node.val);
    if (!node.right || node.right === start) break;
    node = node.right;
  }
  return result;
}

function listToGraph(adjList) {
  if (!adjList || adjList.length === 0) return null;
  const nodes = adjList.map((_, i) => ({ val: i + 1, neighbors: [] }));
  adjList.forEach((neighbors, i) => {
    nodes[i].neighbors = neighbors.map((n) => nodes[n - 1]);
  });
  return nodes[0];
}

function graphToList(node) {
  if (!node) return [];
  const ordered = [];
  const index = new Map();
  const queue = [node];
  index.set(node, 0);
  ordered.push(node);
  while (queue.length > 0) {
    const current = queue.shift();
    for (const neighbor of current.neighbors) {
      if (!index.has(neighbor)) {
        index.set(neighbor, ordered.length);
        ordered.push(neighbor);
        queue.push(neighbor);
      }
    }
  }
  ordered.sort((a, b) => a.val - b.val);
  return ordered.map((item) => item.neighbors.map((neighbor) => neighbor.val));
}

function listToRandomList(pairs) {
  if (!pairs || pairs.length === 0) return null;
  const nodes = pairs.map((pair) => ({ val: pair[0], next: null, random: null }));
  pairs.forEach((pair, i) => {
    if (i + 1 < nodes.length) nodes[i].next = nodes[i + 1];
    if (pair[1] !== null && pair[1] !== undefined) nodes[i].random = nodes[pair[1]];
  });
  return nodes[0];
}

function randomListToList(head) {
  if (!head) return [];
  const nodes = [];
  const index = new Map();
  let current = head;
  while (current) {
    index.set(current, nodes.length);
    nodes.push(current);
    current = current.next;
  }
  return nodes.map((node) => [node.val, node.random ? index.get(node.random) : null]);
}

function jsonToNestedInteger(value) {
  if (typeof value === "number") {
    return {
      isInteger() {
        return true;
      },
      getInteger() {
        return value;
      },
      getList() {
        return [];
      },
    };
  }
  const list = value.map((entry) => jsonToNestedInteger(entry));
  return {
    isInteger() {
      return false;
    },
    getInteger() {
      return 0;
    },
    getList() {
      return list;
    },
  };
}

function jsonToNestedList(values) {
  return values.map((value) => jsonToNestedInteger(value));
}

function mockMountainArray(values) {
  return {
    get(index) {
      return values[index];
    },
    length() {
      return values.length;
    },
  };
}

function convertArg(value, typeName) {
  if (typeName === "listnode") return listToListNode(value);
  if (typeName === "listnode[]") {
    return value.map((item) => (item && item.length ? listToListNode(item) : null));
  }
  if (typeName === "treenode") return listToTree(value);
  if (typeName === "nextnode") return listToNextNode(value);
  if (typeName === "graphnode") return listToGraph(value);
  if (typeName === "randomlistnode") return listToRandomList(value);
  if (typeName === "nestedinteger[]") return jsonToNestedList(value);
  if (typeName === "narynode") return listToNary(value);
  if (typeName === "multilevelnode") return listToMultilevel(value);
  return value;
}

function parseInplaceExpected(expected) {
  const match = /^(\d+),\s*(nums|chars)\s*=\s*\[(.*)\]$/.exec(String(expected).trim());
  if (!match) return null;
  const count = Number(match[1]);
  const field = match[2];
  const raw = match[3];
  if (field === "chars") {
    const prefix = [...raw.matchAll(/"([^"]*)"|'([^']*)'/g)].map((m) => m[1] ?? m[2]);
    return { count, prefix };
  }
  const prefix = raw
    .split(",")
    .map((token) => token.trim())
    .filter((token) => token && token !== "_")
    .map(Number);
  return { count, prefix };
}

function isInplaceExpected(expected) {
  return typeof expected === "string" && (expected.includes(", nums = [") || expected.includes(", chars = ["));
}

function nestedIntegerToValue(item) {
  if (item.isInteger()) {
    return item.getInteger();
  }
  return item.getList().map((entry) => nestedIntegerToValue(entry));
}

function convertResult(value, typeName) {
  if (typeName === "listnode") return listNodeToList(value);
  if (typeName === "treenode") return treeToList(value);
  if (typeName === "treenode[]") {
    if (!value) return [];
    return value.map((item) => treeToList(item));
  }
  if (typeName === "nextnode") return nextNodeToSerialized(value);
  if (typeName === "graphnode") return graphToList(value);
  if (typeName === "randomlistnode") return randomListToList(value);
  if (typeName === "nestedinteger") return nestedIntegerToValue(value);
  if (typeName === "narynode") return naryToList(value);
  if (typeName === "quadnode") return quadTreeToList(value);
  if (typeName === "multilevelnode") return multilevelToList(value);
  if (typeName === "doublytreenode") return doublyTreeNodeToList(value);
  return value;
}

function deepEqual(actual, expected) {
  if (Array.isArray(actual) && Array.isArray(expected)) {
    if (actual.length !== expected.length) {
      return false;
    }
    return actual.every((item, index) => deepEqual(item, expected[index]));
  }
  if (typeof actual === "number" || typeof expected === "number") {
    const actualNumber = Number(actual);
    const expectedNumber = Number(expected);
    if (Number.isFinite(actualNumber) && Number.isFinite(expectedNumber)) {
      return Math.abs(actualNumber - expectedNumber) < 1e-5;
    }
  }
  return JSON.stringify(actual) === JSON.stringify(expected);
}

function treesEqualAnyOrder(actual, expected) {
  const a = [...actual].map((item) => JSON.stringify(item)).sort();
  const b = [...expected].map((item) => JSON.stringify(item)).sort();
  return a.length === b.length && a.every((item, index) => item === b[index]);
}

function loadJson(filePath) {
  const raw = fs.readFileSync(filePath, "utf8").replace(/^\uFEFF/, "");
  return JSON.parse(raw);
}

function orderedArgValues(args, config) {
  const keys = config.paramOrder || Object.keys(args);
  const argTypes = config.types || {};
  return keys.map((key) => convertArg(args[key], argTypes[key]));
}

async function loadSolution(problemDir) {
  const solutionPath = path.join(problemDir, "solution.js");
  const script = fs.readFileSync(solutionPath, "utf8");
  const sandbox = { module: { exports: {} }, exports: {} };
  vm.createContext(sandbox);
  vm.runInContext(script, sandbox, { filename: solutionPath });

  const exported = { ...sandbox.module.exports, ...sandbox.exports };
  for (const [key, value] of Object.entries(sandbox)) {
    if (typeof value === "function" && !["module", "exports"].includes(key)) {
      exported[key] = value;
    }
  }
  if (sandbox.Solution) {
    exported.Solution = sandbox.Solution;
  }
  return { exported, sandbox };
}

function resolveCallable(exported, config) {
  const methodName = config.method;
  if (typeof exported[methodName] === "function") {
    return exported[methodName].bind(exported);
  }
  if (exported.Solution) {
    const solution = new exported.Solution();
    if (typeof solution[methodName] === "function") {
      return (...args) => solution[methodName](...args);
    }
  }
  if (exported.default && typeof exported.default === "function") {
    const maybeClass = exported.default;
    if (maybeClass.prototype && typeof maybeClass.prototype[methodName] === "function") {
      const solution = new maybeClass();
      return (...args) => solution[methodName](...args);
    }
  }
  throw new Error(`Method ${methodName} not found in solution.js`);
}

async function main() {
  const problemDir = path.resolve(process.argv[2]);
  if (!problemDir) {
    console.error("Usage: run_tests.mjs <problem_dir>");
    process.exit(2);
  }

  const config = loadJson(path.join(problemDir, "tests", "config.json"));
  const casesDoc = loadJson(path.join(problemDir, "tests", "cases.json"));
  const check = preRunCheck("javascript", config, casesDoc, {
    hasSolutionFile: fs.existsSync(path.join(problemDir, "solution.js")),
  });
  if (!check.canRun) {
    console.log(`JavaScript tests: ${path.basename(problemDir)}`);
    console.log(`  ${check.message}`);
    process.exit(check.exitCode);
  }

  const { exported, sandbox } = await loadSolution(problemDir);

  if (usesDesignCases(casesDoc) || config.kind === "design") {
    const designClass = config.class || casesDoc.cases[0].operations[0];
    console.log(`JavaScript design tests: ${path.basename(problemDir)} :: ${designClass}`);
    const { passed, total } = runDesignCases(exported, casesDoc);
    console.log(`Result: ${passed}/${total} passed`);
    process.exit(passed === total ? 0 : 1);
  }

  const isZigzagIterator = config.class === "ZigzagIterator";
  const isNestedIterator = config.class === "NestedIterator";
  const isCodecRoundtrip = config.class === "Codec";
  const isEncodeString = config.class === "Solution" && config.method === "encode";
  const fn = isZigzagIterator || isNestedIterator || isCodecRoundtrip || isEncodeString ? null : resolveCallable(exported, config);
  const returnType = config.types?.return;

  console.log(
    isZigzagIterator
      ? `JavaScript tests: ${path.basename(problemDir)} :: ZigzagIterator`
      : isNestedIterator
        ? `JavaScript tests: ${path.basename(problemDir)} :: NestedIterator`
        : isCodecRoundtrip
          ? `JavaScript tests: ${path.basename(problemDir)} :: Codec`
          : `JavaScript tests: ${path.basename(problemDir)} :: ${config.method}()`,
  );

  let passed = 0;
  casesDoc.cases.forEach((testCase, index) => {
    const args = testCase.args || {};
    const keys = (config.paramOrder || Object.keys(args)).filter((key) => key !== "pos" && key !== "bad" && key !== "pick");
    const argTypes = config.types || {};
    let cycleHead = null;
    let actual;
    let naryTreeCompare = false;
    let expected = testCase.expected;

    if (args.listA && args.listB && config.method === "getIntersectionNode") {
      const [headA, headB] = buildIntersectionLists(args);
      actual = intersectNodeToString(fn(headA, headB));
    } else if (args.root && args.p !== undefined && args.q !== undefined && config.method === "lowestCommonAncestor") {
      const root = listToTree(args.root);
      const pNode = findTreeNode(root, args.p);
      const qNode = findTreeNode(root, args.q);
      const result = fn(root, pNode, qNode);
      actual = result ? result.val : null;
    } else if (args.root && args.nodes !== undefined && config.method === "lowestCommonAncestor") {
      const root = listToTree(args.root);
      const nodeList = args.nodes.map((value) => findTreeNode(root, value));
      const result = fn(root, nodeList);
      actual = result ? result.val : null;
    } else if (args.root && args.fromNode !== undefined && args.toNode !== undefined && config.method === "correctBinaryTree") {
      const root = listToTree(args.root);
      const fromNode = findTreeNode(root, args.fromNode);
      const toNode = findTreeNode(root, args.toNode);
      fromNode.right = toNode;
      actual = treeToList(fn(root));
    } else if (args.root && args.leaf !== undefined && config.method === "flipBinaryTree") {
      const root = listToParentTree(args.root);
      const leaf = findParentNode(root, args.leaf);
      actual = treeToList(fn(root, leaf));
    } else if (args.v1 !== undefined && args.v2 !== undefined && config.class === "ZigzagIterator") {
      const iterator = new exported.ZigzagIterator(args.v1, args.v2);
      actual = [];
      while (iterator.hasNext()) {
        actual.push(iterator.next());
      }
    } else if (args.nestedList !== undefined && config.class === "NestedIterator") {
      const iterator = new exported.NestedIterator(jsonToNestedList(args.nestedList));
      actual = [];
      while (iterator.hasNext()) {
        actual.push(iterator.next());
      }
    } else if (args.root && args.p !== undefined && config.method === "inorderSuccessor") {
      const root = listToTree(args.root);
      const pNode = findTreeNode(root, args.p);
      const result = fn(root, pNode);
      actual = result ? result.val : null;
    } else if (args.tree && args.node !== undefined && config.method === "inorderSuccessor") {
      const root = listToParentTree(args.tree);
      const target = findParentNode(root, args.node);
      const result = fn(target);
      actual = result ? result.val : null;
    } else if (args.head && args.node !== undefined && config.method === "deleteNode") {
      const head = listToListNode(args.head);
      const target = findListNode(head, args.node);
      fn(target);
      actual = listNodeToList(head);
    } else if (args.dummy_input !== undefined) {
      const CodecClass = exported.Codec || exported.Solution;
      const codec = new CodecClass();
      actual = codec.decode(codec.encode(args.dummy_input));
    } else if (
      config.class === "Codec" &&
      (args.url !== undefined || args.longUrl !== undefined)
    ) {
      const CodecClass = exported.Codec || exported.Solution;
      const codec = new CodecClass();
      const longUrl = args.url ?? args.longUrl;
      actual = codec.decode(codec.encode(longUrl));
    } else if (
      args.root !== undefined &&
      config.method === "encodeNaryTree" &&
      argTypes.root === "narynode"
    ) {
      const SolutionClass = exported.Solution || exported.default;
      const solution = new SolutionClass();
      const root = listToNary(args.root);
      const binary = solution.encodeNaryTree(root);
      actual = solution.decodeBinaryTree(binary);
      expected = root;
      naryTreeCompare = true;
    } else if (
      args.root !== undefined &&
      config.class === "Codec" &&
      argTypes.root === "narynode"
    ) {
      const CodecClass = exported.Codec || exported.Solution;
      const codec = new CodecClass();
      const root = listToNary(args.root);
      actual = codec.deserialize(codec.encode(root));
      expected = root;
      naryTreeCompare = true;
    } else if (
      args.root !== undefined &&
      config.class === "Codec" &&
      args.p === undefined &&
      args.q === undefined
    ) {
      const CodecClass = exported.Codec || exported.Solution;
      const codec = new CodecClass();
      const root = listToTree(args.root);
      actual = treeToList(codec.deserialize(codec.serialize(root)));
    } else if (args.root !== undefined && config.method === "treeToDoublyList") {
      const root = listToTree(args.root);
      actual = doublyTreeNodeToList(fn(root));
    } else if (args.grid !== undefined && config.method === "construct") {
      actual = quadTreeToList(fn(args.grid));
    } else if (args.root !== undefined && config.method === "levelOrder" && argTypes.root === "narynode") {
      actual = fn(listToNary(args.root));
    } else if (args.head !== undefined && config.method === "flatten" && argTypes.head === "multilevelnode") {
      actual = multilevelToList(fn(listToMultilevel(args.head)));
    } else if (args.s !== undefined && config.method === "encode" && config.class === "Solution") {
      const SolutionClass = exported.Solution || exported.default;
      const solution = new SolutionClass();
      actual = solution.encode(args.s);
    } else if (args.pick !== undefined && config.method === "guessNumber") {
      const pick = args.pick;
      exported.guess = (num) => {
        if (num > pick) return -1;
        if (num < pick) return 1;
        return 0;
      };
      actual = fn(args.n);
    } else if (args.bad !== undefined && config.method === "firstBadVersion") {
      const bad = args.bad;
      exported.isBadVersion = (version) => version >= bad;
      actual = fn(args.n);
    } else if (args.graph !== undefined && config.method === "findCelebrity") {
      const graph = args.graph;
      exported.knows = (personA, personB) => graph[personA][personB] === 1;
      actual = fn(graph.length);
    } else if (args.room !== undefined && config.method === "cleanRoom") {
      const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];
      const robot = {
        room: args.room,
        row: args.row,
        col: args.col,
        direction: 0,
        cleaned: new Set(),
        move() {
          const [dr, dc] = directions[this.direction];
          const nr = this.row + dr;
          const nc = this.col + dc;
          if (nr >= 0 && nr < this.room.length && nc >= 0 && nc < this.room[0].length && this.room[nr][nc] === 1) {
            this.row = nr;
            this.col = nc;
            return true;
          }
          return false;
        },
        turnLeft() {
          this.direction = (this.direction + 3) % 4;
        },
        turnRight() {
          this.direction = (this.direction + 1) % 4;
        },
        clean() {
          this.cleaned.add(`${this.row},${this.col}`);
        },
      };
      fn(robot);
      let allCleaned = true;
      for (let r = 0; r < args.room.length; r += 1) {
        for (let c = 0; c < args.room[r].length; c += 1) {
          if (args.room[r][c] === 1 && !robot.cleaned.has(`${r},${c}`)) {
            allCleaned = false;
          }
        }
      }
      actual = allCleaned ? "Robot cleaned all rooms." : "Robot missed rooms.";
    } else if (config.method === "rand10" && args.n !== undefined) {
      const sequence = testCase.rand7Sequence || [];
      let seqIndex = 0;
      sandbox.rand7 = () => {
        if (seqIndex >= sequence.length) {
          throw new Error("rand7Sequence exhausted");
        }
        const value = sequence[seqIndex];
        seqIndex += 1;
        return value;
      };
      const solution = new exported.Solution();
      actual = [];
      for (let callIndex = 0; callIndex < args.n; callIndex += 1) {
        actual.push(solution.rand10());
      }
    } else {
      const values = keys.map((key) => {
        if (argTypes[key] === "cyclelistnode") {
          cycleHead = listToCycleList(args[key], args.pos ?? -1);
          return cycleHead;
        }
        return convertArg(args[key], argTypes[key]);
      });
      if (keys.includes("nums") && (isInplaceExpected(testCase.expected) || returnType === "void")) {
        const numsIndex = keys.indexOf("nums");
        values[numsIndex] = [...values[numsIndex]];
      }
      if (keys.includes("chars") && (isInplaceExpected(testCase.expected) || returnType === "void")) {
        const charsIndex = keys.indexOf("chars");
        values[charsIndex] = [...values[charsIndex]];
      }
      if (returnType === "void" && keys.includes("s") && Array.isArray(args.s)) {
        const sIndex = keys.indexOf("s");
        values[sIndex] = [...values[sIndex]];
      }
      if (returnType === "void" && keys.includes("arr") && Array.isArray(args.arr)) {
        const arrIndex = keys.indexOf("arr");
        values[arrIndex] = [...values[arrIndex]];
      }
      if (keys.includes("mountainArr") && config.method === "findInMountainArray") {
        const mountainIndex = keys.indexOf("mountainArr");
        values[mountainIndex] = mockMountainArray(args.mountainArr);
      }
      if (returnType === "void" && keys.includes("nums1")) {
        const nums1Index = keys.indexOf("nums1");
        values[nums1Index] = [...values[nums1Index]];
      }
      if (returnType === "void" && keys.includes("board")) {
        const boardIndex = keys.indexOf("board");
        values[boardIndex] = values[boardIndex].map((row) => [...row]);
      }
      if (returnType === "void" && keys.includes("rooms")) {
        const roomsIndex = keys.indexOf("rooms");
        values[roomsIndex] = values[roomsIndex].map((row) => [...row]);
      }
      if (returnType === "void" && keys.includes("matrix")) {
        const matrixIndex = keys.indexOf("matrix");
        values[matrixIndex] = values[matrixIndex].map((row) => [...row]);
      }
      const actualRaw = fn(...values);
      if (returnType === "void") {
        if (keys.includes("nums")) actual = values[keys.indexOf("nums")];
        else if (keys.includes("arr") && Array.isArray(values[keys.indexOf("arr")])) actual = values[keys.indexOf("arr")];
        else if (keys.includes("s") && Array.isArray(values[keys.indexOf("s")])) actual = values[keys.indexOf("s")];
        else if (keys.includes("nums1")) actual = values[keys.indexOf("nums1")];
        else if (keys.includes("board")) actual = values[keys.indexOf("board")];
        else if (keys.includes("rooms")) actual = values[keys.indexOf("rooms")];
        else if (keys.includes("matrix")) actual = values[keys.indexOf("matrix")];
        else if (keys.includes("root")) actual = treeToList(values[keys.indexOf("root")]);
        else if (keys.includes("head")) actual = listNodeToList(values[keys.indexOf("head")]);
        else actual = actualRaw;
      } else if (returnType === "cycleentry") {
        actual = cycleEntryToString(actualRaw, cycleHead);
      } else {
        actual = convertResult(actualRaw, returnType);
      }
      if (isInplaceExpected(expected)) {
        const parsed = parseInplaceExpected(expected);
        const numsIndex = keys.indexOf("nums");
        const charsIndex = keys.indexOf("chars");
        const mutated = numsIndex >= 0 ? values[numsIndex] : values[charsIndex];
        const ok = parsed
          && actual === parsed.count
          && mutated
          && mutated.slice(0, parsed.count).every((value, i) => value === parsed.prefix[i]);
        if (ok) {
          passed += 1;
          console.log(`  PASS case ${index + 1}`);
        } else {
          console.log(`  FAIL case ${index + 1}: expected ${JSON.stringify(expected)}, got ${JSON.stringify(actual)}`);
        }
        return;
      }
    }

    let ok = false;
    if (returnType === "treenode[]" || returnType === "string[][]" || returnType === "string[]" || returnType === "integer[][]" || returnType === "integer[]") {
      ok = treesEqualAnyOrder(actual, expected);
    } else if (config.method === "wiggleSort" && Array.isArray(actual) && isWiggle(actual)) {
      ok = true;
    } else if (naryTreeCompare) {
      ok = naryTreesEqual(actual, expected);
    } else {
      ok = deepEqual(actual, expected);
    }
    if (ok) {
      passed += 1;
      console.log(`  PASS case ${index + 1}`);
    } else {
      console.log(`  FAIL case ${index + 1}: expected ${JSON.stringify(expected)}, got ${JSON.stringify(actual)}`);
    }
  });

  console.log(`Result: ${passed}/${casesDoc.cases.length} passed`);
  process.exit(passed === casesDoc.cases.length ? 0 : 1);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
