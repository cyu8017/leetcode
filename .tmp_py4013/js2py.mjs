import fs from "fs";
import path from "path";
import { parse } from "acorn";

const ROOT = "/Users/cyu/Documents/Git/github-cyu8017/leetcode";

function jsTypeToPy(t) {
  if (!t) return "Any";
  t = t.trim();
  if (t === "void") return "None";
  if (t === "boolean") return "bool";
  if (t === "string") return "str";
  if (t === "number") return "int";
  if (t === "ListNode") return "Optional[ListNode]";
  if (t === "TreeNode") return "Optional[TreeNode]";
  if (t === "Node") return "Optional[Node]";
  const m2 = t.match(/^(.+)\[\]\[\]$/);
  if (m2) return `List[List[${jsTypeToPy(m2[1])}]]`.replace("List[List[int]]", "List[List[int]]");
  const m1 = t.match(/^(.+)\[\]$/);
  if (m1) {
    const inner = jsTypeToPy(m1[1]);
    return `List[${inner}]`;
  }
  return "Any";
}

function parseJsDoc(src) {
  const params = [];
  let ret = null;
  const reParam = /@param\s+\{([^}]+)\}\s+(\w+)/g;
  let m;
  while ((m = reParam.exec(src))) params.push({ name: m[2], type: jsTypeToPy(m[1]) });
  const reRet = /@return\s+\{([^}]+)\}/;
  m = reRet.exec(src);
  if (m) ret = jsTypeToPy(m[1]);
  return { params, ret };
}

function parseHeader(src) {
  const title = (src.match(/LeetCode\s+(\d+)\s*-\s*(.+)/) || [])[0] || "";
  const num = (src.match(/LeetCode\s+(\d+)/) || [])[1] || "";
  const name = (src.match(/LeetCode\s+\d+\s*-\s*(.+)/) || [])[1] || "";
  const url = (src.match(/https:\/\/leetcode\.com\/problems\/[^\s*]+/) || [])[0] || "";
  return { title, num, name: (name || "").trim(), url };
}

const PREC = {
  LogicalORExpression: 1,
  LogicalANDExpression: 2,
  BinaryExpression: 3,
  UnaryExpression: 4,
  UpdateExpression: 4,
  ConditionalExpression: 0,
};

class Emitter {
  constructor() {
    this.indent = 0;
    this.lines = [];
    this.uses = new Set();
    this.varTypes = new Map(); // name -> 'map'|'set'|'list'|'heap'|'obj'|'ns'
    this.needsHeapq = false;
    this.needsMath = false;
    this.needsSimpleNamespace = false;
    this.needsListNode = false;
    this.needsTreeNode = false;
    this.needsNode = false;
    this.helperClasses = [];
    this.inClass = false;
    this.funcDepth = 0;
    this.loopUpdates = []; // stack of update code for continue
  }

  emitLine(s = "") {
    if (s === "") this.lines.push("");
    else this.lines.push("    ".repeat(this.indent) + s);
  }

  withIndent(fn) {
    this.indent++;
    fn();
    this.indent--;
  }

  mark(name, t) {
    if (name) this.varTypes.set(name, t);
  }
  typeOf(name) {
    return this.varTypes.get(name) || null;
  }

  expr(node, parentPrec = 0) {
    if (!node) return "None";
    switch (node.type) {
      case "Identifier":
        if (node.name === "undefined") return "None";
        if (node.name === "Infinity") return "float('inf')";
        if (node.name === "NaN") return "float('nan')";
        return node.name;
      case "Literal": {
        if (node.regex) return `re.compile(${JSON.stringify(node.regex.pattern)})`;
        if (typeof node.value === "boolean") return node.value ? "True" : "False";
        if (typeof node.value === "string") return JSON.stringify(node.value);
        if (node.value === null) return "None";
        if (typeof node.value === "bigint" || (node.bigint !== undefined)) {
          return String(node.bigint ?? node.value).replace(/n$/, "");
        }
        if (node.raw && /n$/.test(node.raw)) return node.raw.slice(0, -1);
        return String(node.value);
      }
      case "TemplateLiteral": {
        if (node.expressions.length === 0) return JSON.stringify(node.quasis[0].value.cooked);
        let s = 'f"';
        for (let i = 0; i < node.quasis.length; i++) {
          s += node.quasis[i].value.cooked.replace(/{/g, "{{").replace(/}/g, "}}");
          if (i < node.expressions.length) s += `{${this.expr(node.expressions[i])}}`;
        }
        return s + '"';
      }
      case "ThisExpression":
        return "self";
      case "ParenthesizedExpression":
        return `(${this.expr(node.expression)})`;
      case "ArrayExpression": {
        if (node.elements.length === 1 && node.elements[0] && node.elements[0].type === "SpreadElement") {
          return `list(${this.expr(node.elements[0].argument)})`;
        }
        return `[${node.elements.map((e) => (e ? this.expr(e) : "None")).join(", ")}]`;
      }
      case "ObjectExpression": {
        this.needsSimpleNamespace = true;
        const parts = node.properties.map((p) => {
          const k = p.key.type === "Identifier" ? p.key.name : this.expr(p.key);
          return `${k}=${this.expr(p.value)}`;
        });
        return `SimpleNamespace(${parts.join(", ")})`;
      }
      case "UnaryExpression": {
        const a = this.expr(node.argument, 4);
        if (node.operator === "!") {
          if (node.argument.type === "CallExpression" &&
              node.argument.callee.type === "MemberExpression" &&
              node.argument.callee.property.name === "has") {
            const obj = this.expr(node.argument.callee.object);
            const key = this.expr(node.argument.arguments[0]);
            return this.wrap(`${key} not in ${obj}`, 3, parentPrec);
          }
          if (a.includes(" in ") && !a.includes("(")) {
            return this.wrap(`not (${a})`, 4, parentPrec);
          }
          return this.wrap(`not ${this.maybeParenCall(a)}`, 4, parentPrec);
        }
        if (node.operator === "+") return a;
        if (node.operator === "-") return this.wrap(`-${this.maybeParenCall(a)}`, 4, parentPrec);
        if (node.operator === "~") return this.wrap(`~${this.maybeParenCall(a)}`, 4, parentPrec);
        if (node.operator === "typeof") return `type(${a}).__name__`;
        if (node.operator === "void") return "None";
        return `${node.operator}${a}`;
      }
      case "UpdateExpression": {
        // as expression: rare; emit i (and we'll miss the update) — prefer statement form
        return this.expr(node.argument);
      }
      case "BinaryExpression": {
        const opMap = {
          "===": "==",
          "!==": "!=",
          "==": "==",
          "!=": "!=",
          "+": "+",
          "-": "-",
          "*": "*",
          "/": "/",
          "%": "%",
          "<": "<",
          ">": ">",
          "<=": "<=",
          ">=": ">=",
          "<<": "<<",
          ">>": ">>",
          ">>>": ">>",
          "&": "&",
          "|": "|",
          "^": "^",
          "**": "**",
          in: "in",
          instanceof: "in",
        };
        let l = this.expr(node.left, 3);
        let r = this.expr(node.right, 3);
        // null/undefined identity
        if ((node.operator === "===" || node.operator === "==") && (r === "None" || l === "None")) {
          return l === "None" ? `${r} is None` : `${l} is None`;
        }
        if ((node.operator === "!==" || node.operator === "!=") && (r === "None" || l === "None")) {
          return l === "None" ? `${r} is not None` : `${l} is not None`;
        }
        // integer division heuristic: Math.floor(x / y) handled in CallExpression
        let op = opMap[node.operator] || node.operator;
        if (node.operator === "/") {
          // keep / as / (true div) — JS is float. For integer-looking we'll still use /
          // LeetCode JS often wants integer via Math.floor
        }
        return this.wrap(`${l} ${op} ${r}`, 3, parentPrec);
      }
      case "LogicalExpression": {
        const op = node.operator === "&&" ? "and" : "or";
        const prec = op === "and" ? 2 : 1;
        let r = this.expr(node.right, prec);
        if (r.startsWith("lambda ")) r = `(${r})`;
        return this.wrap(`${this.expr(node.left, prec)} ${op} ${r}`, prec, parentPrec);
      }
      case "AssignmentExpression": {
        if (node.left.type === "ArrayPattern") {
          const left = node.left.elements.map((e) => this.expr(e)).join(", ");
          if (node.right.type === "ArrayExpression") {
            return `${left} = ${node.right.elements.map((e) => this.expr(e)).join(", ")}`;
          }
          return `${left} = ${this.expr(node.right)}`;
        }
        const op = node.operator === "=" ? "=" : node.operator; // += -= etc already py-like
        return `${this.lvalue(node.left)} ${op} ${this.expr(node.right)}`;
      }
      case "ConditionalExpression": {
        return this.wrap(
          `${this.expr(node.consequent)} if ${this.expr(node.test)} else ${this.expr(node.alternate)}`,
          0,
          parentPrec
        );
      }
      case "MemberExpression":
        return this.member(node);
      case "CallExpression":
        return this.call(node);
      case "NewExpression":
        return this.newExpr(node);
      case "ArrowFunctionExpression":
      case "FunctionExpression":
        return this.funcExpr(node);
      case "SequenceExpression":
        return `(${node.expressions.map((e) => this.expr(e)).join(", ")})`;
      case "SpreadElement":
        return `*${this.expr(node.argument)}`;
      case "AwaitExpression":
        return this.expr(node.argument);
      default:
        return `/*${node.type}*/`;
    }
  }

  maybeParenCall(s) {
    if (/^not |^[+\-~]/.test(s)) return `(${s})`;
    return s;
  }

  wrap(s, prec, parentPrec) {
    if (prec < parentPrec) return `(${s})`;
    return s;
  }

  lvalue(node) {
    if (node.type === "MemberExpression") return this.member(node, true);
    return this.expr(node);
  }

  member(node, asLvalue = false) {
    const obj = this.expr(node.object);
    if (node.computed) {
      return `${obj}[${this.expr(node.property)}]`;
    }
    const prop = node.property.name;
    // this.x
    if (node.object.type === "ThisExpression") return `self.${prop}`;

    const objName = node.object.type === "Identifier" ? node.object.name : null;
    const t = objName ? this.typeOf(objName) : null;

    if (prop === "length") return `len(${obj})`;
    if (prop === "size" && (t === "map" || t === "set")) return `len(${obj})`;

    // Map/Set methods handled in call()
    return `${obj}.${prop}`;
  }

  call(node) {
    const callee = node.callee;
    // Math.xxx
    if (callee.type === "MemberExpression" && !callee.computed && callee.object.type === "Identifier" && callee.object.name === "Math") {
      const m = callee.property.name;
      const args = node.arguments.map((a) => this.expr(a));
      if (m === "max") return `max(${args.join(", ")})`;
      if (m === "min") return `min(${args.join(", ")})`;
      if (m === "abs") return `abs(${args[0]})`;
      if (m === "floor") {
        const a0 = node.arguments[0];
        if (a0 && a0.type === "BinaryExpression" && a0.operator === "/") {
          return `${this.expr(a0.left)} // ${this.expr(a0.right)}`;
        }
        this.needsMath = true;
        return `math.floor(${args[0]})`;
      }
      if (m === "ceil") {
        this.needsMath = true;
        return `math.ceil(${args[0]})`;
      }
      if (m === "round") {
        this.needsMath = true;
        return `round(${args[0]})`;
      }
      if (m === "pow") return `(${args[0]}) ** (${args[1]})`;
      if (m === "log10") {
        this.needsMath = true;
        return `math.log10(${args[0]})`;
      }
      if (m === "log2") {
        this.needsMath = true;
        return `math.log2(${args[0]})`;
      }
      if (m === "log") {
        this.needsMath = true;
        return `math.log(${args.join(", ")})`;
      }
      if (m === "sqrt") {
        this.needsMath = true;
        return `math.sqrt(${args[0]})`;
      }
      if (m === "hypot") {
        this.needsMath = true;
        return `math.hypot(${args.join(", ")})`;
      }
      return `math.${m}(${args.join(", ")})`;
    }
    // Number(x) BigInt(x) String(x)
    if (callee.type === "Identifier") {
      const n = callee.name;
      const args = node.arguments.map((a) => this.expr(a));
      if (n === "Number" || n === "BigInt" || n === "parseInt" || n === "parseFloat") return args[0];
      if (n === "String") return `str(${args[0]})`;
      if (n === "Boolean") return `bool(${args[0]})`;
      if (n === "Array") {
        if (args.length === 1) return `[None] * (${args[0]})`;
        return `[${args.join(", ")}]`;
      }
      if (n === "Object") return args[0] || "{}";
      if (n === "Set") {
        this.uses.add("Set");
        return args.length ? `set(${args[0]})` : "set()";
      }
      if (n === "Map") return args.length ? `dict(${args[0]})` : "{}";
      if (n === "ListNode") {
        this.needsListNode = true;
        return `ListNode(${args.join(", ")})`;
      }
      if (n === "TreeNode") {
        this.needsTreeNode = true;
        return `TreeNode(${args.join(", ")})`;
      }
      if (n === "Node") {
        this.needsNode = true;
        return `Node(${args.join(", ")})`;
      }
      return `${n}(${args.join(", ")})`;
    }

    if (callee.type === "MemberExpression" && !callee.computed &&
        callee.object.type === "Identifier" && callee.object.name === "Array" &&
        callee.property.name === "from") {
      return this.arrayFrom(node);
    }
    if (callee.type === "MemberExpression" && !callee.computed) {
      const prop = callee.property.name;
      const objNode = callee.object;
      const obj = this.expr(objNode);
      const objName = objNode.type === "Identifier" ? objNode.name : null;
      const t = objName ? this.typeOf(objName) : null;
      const args = node.arguments.map((a) => this.expr(a));

      if (prop === "push") {
        if (objNode.type === "ConditionalExpression") {
          return `(${obj}).append(${args.join(", ")})`;
        }
        if (t === "heap") return `${obj}.push(${args.join(", ")})`;
        return `${obj}.append(${args.join(", ")})`;
      }
      if (prop === "pop") {
        if (args.length) return `${obj}.pop(${args[0]})`;
        return `${obj}.pop()`;
      }
      if (prop === "shift") return `${obj}.pop(0)`;
      if (prop === "unshift") return `${obj}.insert(0, ${args[0]})`;
      if (prop === "join") return `${args[0]}.join(${obj})`;
      if (prop === "split") {
        if (args[0] === '""' || args[0] === "''") return `list(${obj})`;
        return `${obj}.split(${args.join(", ")})`;
      }
      if (prop === "slice") return `${obj}[${args[0] || ""}:${args[1] || ""}]`;
      if (prop === "splice") {
        // limited
        if (args.length === 2 && args[1] === "1") return `${obj}.pop(${args[0]})`;
        return `${obj}[${args[0]}:${args[0]} + ${args[1] || "0"}]`;
      }
      if (prop === "indexOf") return `${obj}.index(${args[0]}) if ${args[0]} in ${obj} else -1`;
      if (prop === "includes") return `${args[0]} in ${obj}`;
      if (prop === "startsWith") return `${obj}.startswith(${args[0]})`;
      if (prop === "endsWith") return `${obj}.endswith(${args[0]})`;
      if (prop === "charCodeAt") return `ord(${obj}[${args[0]}])`;
      if (prop === "fromCharCode" && obj === "String") return `chr(${args[0]})`;
      if (prop === "padStart") return `${obj}.zfill(${args[0]})` + (args[1] && args[1] !== '"0"' && args[1] !== "'0'" ? `  # pad ${args[1]}` : "");
      if (prop === "repeat") return `${obj} * ${args[0]}`;
      if (prop === "substring" || prop === "substr") return `${obj}[${args[0]}:${args[1] || ""}]`;
      if (prop === "toString" || prop === "toLocaleString") return `str(${obj})`;
      if (prop === "fill") {
        if (objNode.type === "NewExpression" && objNode.callee.type === "Identifier" && objNode.callee.name === "Array") {
          const n = this.expr(objNode.arguments[0]);
          return `[${args[0]}] * (${n})`;
        }
        return `[${args[0]}] * len(${obj})`;
      }
      if (prop === "map") {
        if (node.arguments[0] && (node.arguments[0].type === "ArrowFunctionExpression" || node.arguments[0].type === "FunctionExpression")) {
          const fn = node.arguments[0];
          const p = (fn.params[0] && fn.params[0].name) || "x";
          let bodyNode = fn.body.type === "BlockStatement" ? null : fn.body;
          if (bodyNode && bodyNode.type === "CallExpression" &&
              bodyNode.callee.type === "MemberExpression" &&
              bodyNode.callee.property.name === "sort") {
            const inner = bodyNode.callee.object;
            if (inner.type === "ArrayExpression" && inner.elements[0] && inner.elements[0].type === "SpreadElement") {
              return `[sorted(${this.expr(inner.elements[0].argument)}) for ${p} in ${obj}]`;
            }
            return `[sorted(${this.expr(inner)}) for ${p} in ${obj}]`;
          }
          const body = bodyNode ? this.expr(bodyNode) : null;
          if (body) return `[${body} for ${p} in ${obj}]`;
        }
        return `list(map(${args[0]}, ${obj}))`;
      }
      if (prop === "filter") {
        if (node.arguments[0] && node.arguments[0].type === "ArrowFunctionExpression") {
          const fn = node.arguments[0];
          const p = (fn.params[0] && fn.params[0].name) || "x";
          const body = fn.body.type === "BlockStatement" ? null : this.expr(fn.body);
          if (body) return `[${p} for ${p} in ${obj} if ${body}]`;
        }
        return `list(filter(${args[0]}, ${obj}))`;
      }
      if (prop === "sort") {
        return this.sortCall(obj, node.arguments[0], objNode);
      }
      if (prop === "reverse") return `${obj}.reverse()`;
      if (prop === "has") return `${args[0]} in ${obj}`;
      if (prop === "get") {
        if (args.length === 1) return `${obj}.get(${args[0]})`;
        return `${obj}.get(${args[0]}, ${args[1]})`;
      }
      if (prop === "set") {
        return `${obj}[${args[0]}] = ${args[1]}`;
      }
      if (prop === "add") return `${obj}.add(${args[0]})`;
      if (prop === "delete" || prop === "remove") {
        if (t === "set" || prop === "delete") return `${obj}.discard(${args[0]})`;
        return `${obj}.remove(${args[0]})`;
      }
      if (prop === "clear") return `${obj}.clear()`;
      if (prop === "keys") return `list(${obj}.keys())`;
      if (prop === "values") return `list(${obj}.values())`;
      if (prop === "entries") return `list(${obj}.items())`;
      if (prop === "charAt") return `${obj}[${args[0]}]`;
      if (prop === "concat") return `(${obj} + ${args[0]})`;
      if (prop === "size" && args.length === 0) return `len(${obj})`;

      return `${obj}.${prop}(${args.join(", ")})`;
    }

    return `${this.expr(callee)}(${node.arguments.map((a) => this.expr(a)).join(", ")})`;
  }

  newExpr(node) {
    const callee = node.callee;
    const name = callee.type === "Identifier" ? callee.name : this.expr(callee);
    const args = node.arguments.map((a) => this.expr(a));
    if (name === "Map") return "{}";
    if (name === "Set") return args.length ? `set(${args[0]})` : "set()";
    if (name === "Array") {
      if (node.arguments.length === 1) return `[None] * (${args[0]})`;
      return `[${args.join(", ")}]`;
    }
    if (name === "ListNode") {
      this.needsListNode = true;
      return `ListNode(${args.join(", ")})`;
    }
    if (name === "TreeNode") {
      this.needsTreeNode = true;
      return `TreeNode(${args.join(", ")})`;
    }
    if (name === "Node") {
      this.needsNode = true;
      return `Node(${args.join(", ")})`;
    }
    if (name === "MinHeap" || name === "Heap") {
      return `${name}(${args.join(", ")})`;
    }
    return `${name}(${args.join(", ")})`;
  }

  arrayFrom(node) {
    const spec = node.arguments[0];
    let nExpr = "0";
    if (spec && spec.type === "ObjectExpression") {
      const lp = spec.properties.find((p) => (p.key.name || p.key.value) === "length");
      if (lp) nExpr = this.expr(lp.value);
    } else if (spec) {
      nExpr = `len(${this.expr(spec)})`;
    }
    const cb = node.arguments[1];
    if (!cb) return `list(range(${nExpr}))`;
    if (cb.type === "ArrowFunctionExpression" || cb.type === "FunctionExpression") {
      const params = cb.params.map((p) => (p.type === "Identifier" ? p.name : "_"));
      const bodyNode = cb.body.type === "BlockStatement" ? null : cb.body;
      if (bodyNode) {
        const body = this.expr(bodyNode);
        if (params.length >= 2) return `[${body} for ${params[1]} in range(${nExpr})]`;
        return `[${body} for _ in range(${nExpr})]`;
      }
    }
    return `[${this.expr(cb)}() for _ in range(${nExpr})]`;
  }

  sortCall(obj, cmp, objNode) {
    if (!cmp) return `${obj}.sort()`;
    // slice().sort(...)
    if (objNode && objNode.type === "CallExpression" &&
        objNode.callee.type === "MemberExpression" &&
        objNode.callee.property.name === "slice") {
      const inner = this.expr(objNode.callee.object);
      const key = this.sortKey(cmp);
      if (key === "asc") return `sorted(${inner})`;
      if (key === "desc") return `sorted(${inner}, reverse=True)`;
      if (key) return `sorted(${inner}, key=${key})`;
      return `sorted(${inner})`;
    }
    const key = this.sortKey(cmp);
    if (key === "asc") return `${obj}.sort()`;
    if (key === "desc") return `${obj}.sort(reverse=True)`;
    if (key) return `${obj}.sort(key=${key})`;
    return `${obj}.sort()`;
  }

  sortKey(cmp) {
    if (!cmp || (cmp.type !== "ArrowFunctionExpression" && cmp.type !== "FunctionExpression")) return null;
    const body = cmp.body.type === "BlockStatement"
      ? (cmp.body.body[0] && cmp.body.body[0].type === "ReturnStatement" ? cmp.body.body[0].argument : null)
      : cmp.body;
    if (!body) return null;
    const [a, b] = cmp.params.map((p) => p.name);
    // a - b
    if (body.type === "BinaryExpression" && body.operator === "-" &&
        body.left.type === "Identifier" && body.left.name === a &&
        body.right.type === "Identifier" && body.right.name === b) return "asc";
    // b - a
    if (body.type === "BinaryExpression" && body.operator === "-" &&
        body.left.type === "Identifier" && body.left.name === b &&
        body.right.type === "Identifier" && body.right.name === a) return "desc";
    // growTime[b] - growTime[a]
    if (body.type === "BinaryExpression" && body.operator === "-" &&
        body.left.type === "MemberExpression" && body.right.type === "MemberExpression" &&
        body.left.computed && body.right.computed &&
        this.expr(body.left.object) === this.expr(body.right.object) &&
        body.left.property.type === "Identifier" && body.left.property.name === b &&
        body.right.property.type === "Identifier" && body.right.property.name === a) {
      return `lambda ${a}: -${this.expr(body.left.object)}[${a}]`;
    }
    // a[0] - b[0] || a[1] - b[1] ...
    if (body.type === "LogicalExpression" || (body.type === "BinaryExpression" && body.operator === "-")) {
      const parts = [];
      const walk = (n) => {
        if (n.type === "LogicalExpression" && n.operator === "||") {
          walk(n.left); walk(n.right); return;
        }
        if (n.type === "BinaryExpression" && n.operator === "-" &&
            n.left.type === "MemberExpression" && n.right.type === "MemberExpression") {
          parts.push(this.expr(n.left).replace(a, "x"));
        }
      };
      walk(body);
      if (parts.length) return `lambda x: (${parts.join(", ")})`;
    }
    return null;
  }

  hoistExpr(node) {
    if (!node) return { pre: [], post: [], code: "None" };
    if (node.type === "ParenthesizedExpression") {
      const inner = this.hoistExpr(node.expression);
      return { pre: inner.pre, post: inner.post, code: `(${inner.code})` };
    }
    if (node.type === "UpdateExpression") {
      const inner = this.hoistExpr(node.argument);
      const op = node.operator === "++" ? "+=" : "-=";
      const upd = `${inner.code} ${op} 1`;
      if (node.prefix) return { pre: [...inner.pre, upd], post: inner.post, code: inner.code };
      return { pre: inner.pre, post: [...inner.post, upd], code: inner.code };
    }
    if (node.type === "AssignmentExpression") {
      const L = this.hoistExpr(node.left);
      const R = this.hoistExpr(node.right);
      const op = node.operator === "=" ? "=" : node.operator;
      if (node.left.type === "ArrayPattern") {
        return { pre: [...L.pre, ...R.pre], post: [...L.post, ...R.post], code: this.expr(node) };
      }
      return { pre: [...L.pre, ...R.pre], post: [...L.post, ...R.post], code: `${L.code} ${op} ${R.code}` };
    }
    if (node.type === "BinaryExpression" || node.type === "LogicalExpression") {
      const L = this.hoistExpr(node.left);
      const R = this.hoistExpr(node.right);
      return { pre: [...L.pre, ...R.pre], post: [...L.post, ...R.post], code: this.expr(node) };
    }
    if (node.type === "UnaryExpression") {
      const A = this.hoistExpr(node.argument);
      return { pre: A.pre, post: A.post, code: this.expr(node) };
    }
    if (node.type === "MemberExpression") {
      const O = this.hoistExpr(node.object);
      const P = node.computed ? this.hoistExpr(node.property) : { pre: [], post: [], code: "" };
      const code = node.computed ? `${O.code}[${P.code}]` : this.member(node);
      // if property has updates, rebuild member with hoisted property
      if (node.computed && (P.pre.length || P.post.length || O.pre.length || O.post.length)) {
        return { pre: [...O.pre, ...P.pre], post: [...O.post, ...P.post], code: `${O.code}[${P.code}]` };
      }
      return { pre: [...O.pre, ...P.pre], post: [...O.post, ...P.post], code };
    }
    if (node.type === "CallExpression") {
      const C = this.hoistExpr(node.callee);
      const args = node.arguments.map((a) => this.hoistExpr(a));
      const has = C.pre.length || C.post.length || args.some((a) => a.pre.length || a.post.length);
      if (!has) return { pre: [], post: [], code: this.expr(node) };
      return {
        pre: [...C.pre, ...args.flatMap((a) => a.pre)],
        post: [...C.post, ...args.flatMap((a) => a.post)],
        code: this.expr(node),
      };
    }
    if (node.type === "ConditionalExpression") {
      // don't hoist across branches
      return { pre: [], post: [], code: this.expr(node) };
    }
    return { pre: [], post: [], code: this.expr(node) };
  }

  emitHoisted(h, asStmt = true) {
    for (const s of h.pre) this.emitLine(s);
    if (asStmt) this.emitLine(h.code);
    for (const s of h.post) this.emitLine(s);
  }

  funcExpr(node) {
    const params = node.params.map((p) => {
      if (p.type === "AssignmentPattern") return `${p.left.name}=${this.expr(p.right)}`;
      if (p.type === "Identifier") return p.name;
      return "arg";
    });
    if (node.body.type !== "BlockStatement") {
      return `lambda ${params.join(", ")}: ${this.expr(node.body)}`;
    }
    // block arrow used inline — emit as nested later; as expr use lambda if single return
    const body = node.body.body;
    if (body.length === 1 && body[0].type === "ReturnStatement") {
      return `lambda ${params.join(", ")}: ${this.expr(body[0].argument)}`;
    }
    return `lambda ${params.join(", ")}: None  # complex`;
  }

  stmt(node) {
    if (!node) return;
    switch (node.type) {
      case "FunctionDeclaration":
        this.funcDecl(node);
        break;
      case "VariableDeclaration":
        this.varDecl(node);
        break;
      case "ExpressionStatement": {
        const e = node.expression;
        if (e.type === "UpdateExpression") {
          const a = this.expr(e.argument);
          this.emitLine(`${a} ${e.operator === "++" ? "+=" : "-="} 1`);
          return;
        }
        if (e.type === "CallExpression" && e.callee.type === "MemberExpression" && e.callee.property.name === "set") {
          this.emitLine(this.call(e));
          return;
        }
        const h = this.hoistExpr(e);
        this.emitHoisted(h, true);
        break;
      }
      case "ReturnStatement": {
        if (!node.argument) {
          this.emitLine("return");
          break;
        }
        const h = this.hoistExpr(node.argument);
        for (const s of h.pre) this.emitLine(s);
        this.emitLine(`return ${h.code}`);
        for (const s of h.post) this.emitLine(s);
        break;
      }
      case "IfStatement": {
        const h = this.hoistExpr(node.test);
        for (const s of h.pre) this.emitLine(s);
        this.emitLine(`if ${this.testFromCode(h.code, node.test)}:`);
        this.withIndent(() => this.blockOrStmt(node.consequent));
        for (const s of h.post) this.emitLine(s);
        if (node.alternate) {
          if (node.alternate.type === "IfStatement") {
            const h2 = this.hoistExpr(node.alternate.test);
            for (const s of h2.pre) this.emitLine(s);
            this.emitLine(`elif ${this.testFromCode(h2.code, node.alternate.test)}:`);
            this.withIndent(() => this.blockOrStmt(node.alternate.consequent));
            for (const s of h2.post) this.emitLine(s);
            let alt = node.alternate.alternate;
            while (alt && alt.type === "IfStatement") {
              const h3 = this.hoistExpr(alt.test);
              for (const s of h3.pre) this.emitLine(s);
              this.emitLine(`elif ${this.testFromCode(h3.code, alt.test)}:`);
              this.withIndent(() => this.blockOrStmt(alt.consequent));
              for (const s of h3.post) this.emitLine(s);
              alt = alt.alternate;
            }
            if (alt) {
              this.emitLine("else:");
              this.withIndent(() => this.blockOrStmt(alt));
            }
          } else {
            this.emitLine("else:");
            this.withIndent(() => this.blockOrStmt(node.alternate));
          }
        }
        break;
      }
      case "WhileStatement":
        this.emitLine(`while ${this.test(node.test)}:`);
        this.withIndent(() => this.blockOrStmt(node.body));
        break;
      case "DoWhileStatement":
        this.emitLine("while True:");
        this.withIndent(() => {
          this.blockOrStmt(node.body);
          this.emitLine(`if not (${this.test(node.test)}):`);
          this.withIndent(() => this.emitLine("break"));
        });
        break;
      case "ForStatement":
        this.forStmt(node);
        break;
      case "ForOfStatement":
        this.forOf(node);
        break;
      case "ForInStatement":
        this.emitLine(`for ${this.forLeft(node.left)} in ${this.expr(node.right)}:`);
        this.withIndent(() => this.blockOrStmt(node.body));
        break;
      case "BreakStatement":
        this.emitLine("break");
        break;
      case "ContinueStatement":
        if (this.loopUpdates.length && this.loopUpdates[this.loopUpdates.length - 1]) {
          this.emitLine(this.loopUpdates[this.loopUpdates.length - 1]);
        }
        this.emitLine("continue");
        break;
      case "BlockStatement":
        for (const s of node.body) this.stmt(s);
        break;
      case "EmptyStatement":
        break;
      case "ThrowStatement":
        this.emitLine(`raise Exception(${this.expr(node.argument)})`);
        break;
      case "ClassDeclaration":
        this.classDecl(node);
        break;
      default:
        this.emitLine(`# unhandled ${node.type}`);
    }
  }

  testFromCode(code, node) {
    if (node && node.type === "MemberExpression" && !node.computed && node.property.name === "length") {
      return this.expr(node.object);
    }
    return code === "true" ? "True" : code === "false" ? "False" : code;
  }

  test(node) {
    // while (q.length) → while q
    if (node.type === "MemberExpression" && !node.computed && node.property.name === "length") {
      return this.expr(node.object);
    }
    if (node.type === "UnaryExpression" && node.operator === "!" && node.argument.type === "MemberExpression" && node.argument.property.name === "length") {
      return `not ${this.expr(node.argument.object)}`;
    }
    if (node.type === "Literal" && node.value === true) return "True";
    if (node.type === "Literal" && node.value === false) return "False";
    return this.expr(node);
  }

  blockOrStmt(node) {
    if (!node) {
      this.emitLine("pass");
      return;
    }
    if (node.type === "BlockStatement") {
      if (node.body.length === 0) this.emitLine("pass");
      else for (const s of node.body) this.stmt(s);
    } else {
      this.stmt(node);
    }
  }

  forLeft(left) {
    if (left.type === "VariableDeclaration") {
      const d = left.declarations[0];
      if (d.id.type === "ArrayPattern") return d.id.elements.map((e) => e.name).join(", ");
      return d.id.name;
    }
    if (left.type === "ArrayPattern") return left.elements.map((e) => e.name).join(", ");
    return this.expr(left);
  }

  forOf(node) {
    const left = this.forLeft(node.left);
    let right = this.expr(node.right);
    const rname = node.right.type === "Identifier" ? node.right.name : null;
    const t = rname ? this.typeOf(rname) : null;
    if (t === "map" && left.includes(",")) right = `${right}.items()`;
    this.emitLine(`for ${left} in ${right}:`);
    this.withIndent(() => this.blockOrStmt(node.body));
  }

  isRangeFor(node) {
    if (!node.init || !node.test || !node.update) return null;
    let name = null;
    let start = "0";
    if (node.init.type === "VariableDeclaration" && node.init.declarations.length === 1) {
      const d = node.init.declarations[0];
      if (d.id.type !== "Identifier") return null;
      name = d.id.name;
      start = d.init ? this.expr(d.init) : "0";
    } else if (node.init.type === "AssignmentExpression" && node.init.left.type === "Identifier") {
      name = node.init.left.name;
      start = this.expr(node.init.right);
    } else return null;

    if (node.test.type !== "BinaryExpression") return null;
    if (node.test.left.type !== "Identifier" || node.test.left.name !== name) return null;
    const endExpr = this.expr(node.test.right);
    const op = node.test.operator;

    let step = null;
    const upd = node.update;
    if (upd.type === "UpdateExpression" && upd.argument.type === "Identifier" && upd.argument.name === name) {
      step = upd.operator === "++" ? "1" : "-1";
    } else if (
      upd.type === "AssignmentExpression" &&
      upd.left.type === "Identifier" &&
      upd.left.name === name
    ) {
      if (upd.operator === "+=") step = this.expr(upd.right);
      else if (upd.operator === "-=") step = `-(${this.expr(upd.right)})`;
      else return null;
    } else return null;

    let stop;
    if (step === "1" || (step !== "-1" && !String(step).startsWith("-"))) {
      if (op === "<") stop = endExpr;
      else if (op === "<=") stop = `(${endExpr}) + 1`;
      else return null;
    } else {
      if (op === ">=") stop = `(${endExpr}) - 1`;
      else if (op === ">") stop = endExpr;
      else return null;
    }
    return { name, start, stop, step };
  }

  forStmt(node) {
    const rng = this.isRangeFor(node);
    if (rng) {
      let r = `range(${rng.start}, ${rng.stop})`;
      if (rng.step !== "1") r = `range(${rng.start}, ${rng.stop}, ${rng.step})`;
      if (rng.start === "0" && rng.step === "1") r = `range(${rng.stop})`;
      this.emitLine(`for ${rng.name} in ${r}:`);
      this.withIndent(() => this.blockOrStmt(node.body));
      return;
    }
    // generic for → while
    if (node.init) {
      if (node.init.type === "VariableDeclaration") this.varDecl(node.init);
      else this.emitLine(this.expr(node.init));
    }
    const updateCode = node.update
      ? node.update.type === "UpdateExpression"
        ? `${this.expr(node.update.argument)} ${node.update.operator === "++" ? "+=" : "-="} 1`
        : this.expr(node.update)
      : "";
    this.emitLine(`while ${node.test ? this.test(node.test) : "True"}:`);
    this.loopUpdates.push(updateCode);
    this.withIndent(() => {
      this.blockOrStmt(node.body);
      if (updateCode) this.emitLine(updateCode);
    });
    this.loopUpdates.pop();
  }

  inferTypeFromInit(init) {
    if (!init) return null;
    if (init.type === "NewExpression" && init.callee.type === "Identifier") {
      const n = init.callee.name;
      if (n === "Map") return "map";
      if (n === "Set") return "set";
      if (n === "Array") return "list";
      if (n === "MinHeap") return "heap";
    }
    if (init.type === "ArrayExpression") return "list";
    if (init.type === "ObjectExpression") return "ns";
    if (init.type === "CallExpression" && init.callee.type === "Identifier" && init.callee.name === "Set") return "set";
    return null;
  }

  varDecl(node) {
    for (const d of node.declarations) {
      if (d.id.type === "ArrayPattern") {
        const names = d.id.elements.map((e) => e.name).join(", ");
        if (d.init && d.init.type === "ArrayExpression") {
          this.emitLine(`${names} = ${d.init.elements.map((e) => this.expr(e)).join(", ")}`);
        } else {
          this.emitLine(`${names} = ${this.expr(d.init)}`);
        }
        continue;
      }
      const name = d.id.name;
      if (!d.init) {
        this.emitLine(`${name} = None`);
        continue;
      }
      // function assigned
      if (d.init.type === "FunctionExpression" || (d.init.type === "ArrowFunctionExpression" && d.init.body.type === "BlockStatement" && !(d.init.body.body.length === 1 && d.init.body.body[0].type === "ReturnStatement"))) {
        this.funcDecl({
          type: "FunctionDeclaration",
          id: { type: "Identifier", name },
          params: d.init.params,
          body: d.init.body.type === "BlockStatement" ? d.init.body : { type: "BlockStatement", body: [{ type: "ReturnStatement", argument: d.init.body }] },
        });
        continue;
      }
      const t = this.inferTypeFromInit(d.init);
      if (t) this.mark(name, t);
      // new Array(n).fill(x)
      if (
        d.init.type === "CallExpression" &&
        d.init.callee.type === "MemberExpression" &&
        d.init.callee.property.name === "fill" &&
        d.init.callee.object.type === "NewExpression" &&
        d.init.callee.object.callee.name === "Array"
      ) {
        const n = this.expr(d.init.callee.object.arguments[0]);
        const v = this.expr(d.init.arguments[0]);
        this.mark(name, "list");
        this.emitLine(`${name} = [${v}] * (${n})`);
        continue;
      }
      // [...have]
      if (d.init.type === "ArrayExpression" && d.init.elements.length === 1 && d.init.elements[0] && d.init.elements[0].type === "SpreadElement") {
        this.mark(name, "list");
        this.emitLine(`${name} = list(${this.expr(d.init.elements[0].argument)})`);
        continue;
      }
      this.emitLine(`${name} = ${this.expr(d.init)}`);
    }
  }

  funcDecl(node, { asMethod = false, className = null } = {}) {
    const name = node.id ? node.id.name : "fn";
    const params = node.params.map((p) => {
      if (p.type === "AssignmentPattern") return `${p.left.name}=${this.expr(p.right)}`;
      if (p.type === "Identifier") return p.name;
      if (p.type === "RestElement") return `*${p.argument.name}`;
      return "arg";
    });
    const first = asMethod || (this.inClass && this.funcDepth === 0) ? "self" : "";
    const plist = [first, ...params].filter(Boolean).join(", ");
    this.emitLine(`def ${name}(${plist}):`);
    this.funcDepth++;
    this.withIndent(() => {
      if (node.body.body.length === 0) this.emitLine("pass");
      else for (const s of node.body.body) this.stmt(s);
    });
    this.funcDepth--;
    this.emitLine("");
  }

  classDecl(node) {
    this.emitLine(`class ${node.id.name}:`);
    const prev = this.inClass;
    this.inClass = true;
    this.withIndent(() => {
      if (node.body.body.length === 0) this.emitLine("pass");
      for (const m of node.body.body) {
        if (m.type !== "MethodDefinition") continue;
        const fname = m.kind === "constructor" ? "__init__" : m.key.name;
        const params = m.value.params.map((p) => (p.type === "Identifier" ? p.name : "arg"));
        this.emitLine(`def ${fname}(self${params.length ? ", " + params.join(", ") : ""}):`);
        this.funcDepth++;
        this.withIndent(() => {
          if (m.value.body.body.length === 0) this.emitLine("pass");
          else for (const s of m.value.body.body) this.stmt(s);
        });
        this.funcDepth--;
        this.emitLine("");
      }
    });
    this.inClass = prev;
  }
}

function convertPrototypeHeap(ast, em) {
  // collect function MinHeap + prototype assignments
}

function convertFile(folder) {
  const dir = path.join(ROOT, folder);
  const jsPath = path.join(dir, "solution.js");
  const cfg = JSON.parse(fs.readFileSync(path.join(dir, "tests/config.json"), "utf8"));
  let src = fs.readFileSync(jsPath, "utf8");
  // strip BOM
  if (src.charCodeAt(0) === 0xfeff) src = src.slice(1);

  const header = parseHeader(src);
  const jsdoc = parseJsDoc(src);

  // SQL
  if (/var\s+QUERY\s*=/.test(src) && !/var\s+\w+\s*=\s*function/.test(src)) {
    const m = src.match(/var\s+QUERY\s*=\s*`([\s\S]*?)`;?/);
    const q = m ? m[1].replace(/\s+$/, "") : "";
    return [
      `# LeetCode ${header.num} - ${header.name}`,
      `# ${header.url}`,
      "",
      "QUERY = \"\"\"",
      q,
      "\"\"\"",
      "",
    ].join("\n");
  }

  // rewrite 2n bigint literals for acorn (already supports?)
  let parseSrc = src.replace(/\/\*[\s\S]*?\*\//g, (c) => c.replace(/[^\n]/g, " "));

  let ast;
  try {
    ast = parse(parseSrc, { ecmaVersion: 2022, sourceType: "script", allowReturnOutsideFunction: true, preserveParens: true });
  } catch (e) {
    throw new Error(`${folder} parse: ${e.message}`);
  }

  const em = new Emitter();
  if (/ListNode/.test(src)) em.needsListNode = true;
  if (/TreeNode/.test(src) && !/function TreeNode/.test(src.replace(/\/\*[\s\S]*?\*\//g, ""))) {
    if (/new TreeNode|@param \{TreeNode|@return \{TreeNode/.test(src)) em.needsTreeNode = true;
  }
  if (/\bTreeNode\b/.test(src)) em.needsTreeNode = true;

  // Top-level: FunctionDeclaration helpers, prototype assignments, var functions, classes
  const topFuncs = [];
  const protoMethods = new Map(); // Class -> [{name, node}]
  const ctors = [];
  const mainVars = [];
  const classes = [];

  for (const node of ast.body) {
    if (node.type === "FunctionDeclaration") {
      ctors.push(node);
    } else if (node.type === "ClassDeclaration") {
      classes.push(node);
    } else if (
      node.type === "ExpressionStatement" &&
      node.expression.type === "AssignmentExpression" &&
      node.expression.left.type === "MemberExpression" &&
      node.expression.left.object.type === "MemberExpression" &&
      node.expression.left.object.property.name === "prototype"
    ) {
      const cls = node.expression.left.object.object.name;
      const meth = node.expression.left.property.name;
      if (!protoMethods.has(cls)) protoMethods.set(cls, []);
      protoMethods.get(cls).push({ name: meth, fn: node.expression.right });
    } else if (node.type === "VariableDeclaration") {
      mainVars.push(node);
    } else if (node.type === "ExpressionStatement") {
      // ignore
    }
  }

  // Emit helper constructor+prototype as class
  for (const ctor of ctors) {
    const cls = ctor.id.name;
    const methods = protoMethods.get(cls) || [];
    em.emitLine(`class ${cls}:`);
    em.inClass = true;
    em.withIndent(() => {
      const params = ctor.params.map((p) => {
        if (p.type === "AssignmentPattern") return `${p.left.name}=${em.expr(p.right)}`;
        return p.name;
      });
      em.emitLine(`def __init__(self${params.length ? ", " + params.join(", ") : ""}):`);
      em.funcDepth++;
      em.withIndent(() => {
        if (ctor.body.body.length === 0) em.emitLine("pass");
        else for (const s of ctor.body.body) em.stmt(s);
      });
      em.funcDepth--;
      em.emitLine("");
      for (const { name, fn } of methods) {
        const ps = fn.params.map((p) => (p.type === "Identifier" ? p.name : "arg"));
        em.emitLine(`def ${name}(self${ps.length ? ", " + ps.join(", ") : ""}):`);
        em.funcDepth++;
        em.withIndent(() => {
          if (fn.body.type === "BlockStatement") {
            if (fn.body.body.length === 0) em.emitLine("pass");
            else for (const s of fn.body.body) em.stmt(s);
          } else {
            em.emitLine(`return ${em.expr(fn.body)}`);
          }
        });
        em.funcDepth--;
        em.emitLine("");
      }
    });
    em.inClass = false;
    em.emitLine("");
  }

  for (const c of classes) em.classDecl(c);

  // Main solution functions
  const solutionMethods = [];
  for (const vd of mainVars) {
    for (const d of vd.declarations) {
      if (!d.init) continue;
      if (d.init.type === "FunctionExpression" || d.init.type === "ArrowFunctionExpression") {
        solutionMethods.push({ name: d.id.name, fn: d.init });
      }
    }
  }

  const isDesign = cfg.kind === "design" || (cfg.class && cfg.class !== "Solution" && cfg.class !== "ListNode" && cfg.class !== "TreeNode");

  if (!isDesign && solutionMethods.length) {
    em.emitLine("class Solution:");
    em.inClass = true;
    em.withIndent(() => {
      for (const { name, fn } of solutionMethods) {
        const methodName =
          cfg.method && !["solve", "__init__", "TreeNode", "ListNode"].includes(cfg.method)
            ? cfg.method
            : name;
        const params = fn.params.map((p, i) => {
          const pname = p.type === "Identifier" ? p.name : p.left ? p.left.name : `arg${i}`;
          const jd = jsdoc.params.find((x) => x.name === pname);
          const typ = jd ? jd.type : "Any";
          if (typ.includes("List") || typ.includes("Optional") || typ === "Any") {
            if (typ.includes("List")) em.uses.add("List");
            if (typ.includes("Optional")) em.uses.add("Optional");
            if (typ === "Any") em.uses.add("Any");
          }
          return `${pname}: ${typ}`;
        });
        let ret = jsdoc.ret || "Any";
        if (ret.includes("List")) em.uses.add("List");
        if (ret.includes("Optional")) em.uses.add("Optional");
        if (ret === "Any") em.uses.add("Any");
        em.emitLine(`def ${methodName}(self, ${params.join(", ")}) -> ${ret}:`);
        em.funcDepth++;
        em.withIndent(() => {
          const body = fn.body.type === "BlockStatement" ? fn.body.body : [{ type: "ReturnStatement", argument: fn.body }];
          if (body.length === 0) em.emitLine("pass");
          else for (const s of body) em.stmt(s);
        });
        em.funcDepth--;
        em.emitLine("");
      }
    });
    em.inClass = false;
  }

  const typing = [];
  if (em.uses.has("List") || em.needsListNode || em.needsTreeNode) typing.push("List");
  if (em.uses.has("Optional") || em.needsListNode || em.needsTreeNode || em.needsNode) typing.push("Optional");
  if (em.uses.has("Any")) typing.push("Any");

  const preamble = [];
  preamble.push(`# LeetCode ${header.num} - ${header.name}`);
  preamble.push(`# ${header.url}`);
  preamble.push("");
  if (em.needsMath) preamble.push("import math");
  if (em.needsSimpleNamespace) preamble.push("from types import SimpleNamespace");
  if (typing.length) preamble.push(`from typing import ${[...new Set(typing)].join(", ")}`);
  if (em.needsMath || em.needsSimpleNamespace || typing.length) {
    if (preamble[preamble.length - 1] !== "") preamble.push("");
  }

  if (em.needsListNode) {
    preamble.push("class ListNode:");
    preamble.push("    def __init__(self, val=0, next=None):");
    preamble.push("        self.val = val");
    preamble.push("        self.next = next");
    preamble.push("");
  }
  if (em.needsTreeNode) {
    preamble.push("class TreeNode:");
    preamble.push("    def __init__(self, val=0, left=None, right=None):");
    preamble.push("        self.val = val");
    preamble.push("        self.left = left");
    preamble.push("        self.right = right");
    preamble.push("");
  }
  if (em.needsNode) {
    preamble.push("class Node:");
    preamble.push("    def __init__(self, val=0, neighbors=None):");
    preamble.push("        self.val = val");
    preamble.push("        self.neighbors = neighbors if neighbors is not None else []");
    preamble.push("");
  }

  let body = em.lines.join("\n");
  // cleanup double blanks
  body = body.replace(/\n{3,}/g, "\n\n");
  let out = preamble.join("\n") + body;
  if (!out.endsWith("\n")) out += "\n";
  // no BOM
  return out;
}

const folders = fs.readFileSync(path.join(ROOT, ".tmp_py4013/batch_01.txt"), "utf8").trim().split("\n");
const only = process.argv.slice(2);
const list = only.length ? only : folders;

let ok = 0, fail = [];
for (const folder of list) {
  try {
    const py = convertFile(folder);
    if (only.length) {
      console.log(py);
    } else {
      fs.writeFileSync(path.join(ROOT, folder, "solution.py"), py, { encoding: "utf8" });
    }
    ok++;
  } catch (e) {
    fail.push([folder, e.message]);
    console.error("FAIL", folder, e.message);
  }
}
if (!only.length) console.error(`wrote ${ok} failed ${fail.length}`);
