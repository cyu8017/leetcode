"use strict";
// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/
// @ts-nocheck
class ExprNode {
    constructor(val, left, right) {
        this.val = val === undefined ? " " : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}
function expTree(s) {
    const nodes = [];
    const ops = [];
    const priority = { "+": 1, "-": 1, "*": 2, "/": 2 };
    const apply = () => {
        const op = ops.pop();
        const right = nodes.pop();
        const left = nodes.pop();
        nodes.push(new ExprNode(op, left, right));
    };
    for (const ch of s) {
        if (ch >= "0" && ch <= "9") {
            nodes.push(new ExprNode(ch));
        }
        else if (ch === "(") {
            ops.push(ch);
        }
        else if (ch === ")") {
            while (ops[ops.length - 1] !== "(")
                apply();
            ops.pop();
        }
        else {
            while (ops.length && ops[ops.length - 1] !== "(" && priority[ops[ops.length - 1]] >= priority[ch]) {
                apply();
            }
            ops.push(ch);
        }
    }
    while (ops.length)
        apply();
    return nodes[0];
}
