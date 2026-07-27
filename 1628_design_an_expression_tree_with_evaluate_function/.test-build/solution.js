"use strict";
// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/
Object.defineProperty(exports, "__esModule", { value: true });
exports.TreeBuilder = exports.Node = void 0;
class Node {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
    evaluate() {
        if (!"+-*/".includes(this.val))
            return Number(this.val);
        const a = this.left.evaluate();
        const b = this.right.evaluate();
        if (this.val === "+")
            return a + b;
        if (this.val === "-")
            return a - b;
        if (this.val === "*")
            return a * b;
        return Math.trunc(a / b);
    }
}
exports.Node = Node;
class TreeBuilder {
    expTree(postfix) {
        const stack = [];
        for (const token of postfix) {
            const node = new Node(token);
            if ("+-*/".includes(token)) {
                node.right = stack.pop();
                node.left = stack.pop();
            }
            stack.push(node);
        }
        return stack[stack.length - 1];
    }
}
exports.TreeBuilder = TreeBuilder;
function expTree(postfix) {
    return new TreeBuilder().expTree(postfix).evaluate();
}
