// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

class Node {
    /**
     * @param {string} val
     * @param {Node|null} left
     * @param {Node|null} right
     */
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    /**
     * @return {number}
     */
    evaluate() {
        if (!"+-*/".includes(this.val)) return Number(this.val);
        const a = this.left.evaluate();
        const b = this.right.evaluate();
        if (this.val === "+") return a + b;
        if (this.val === "-") return a - b;
        if (this.val === "*") return a * b;
        return Math.trunc(a / b);
    }
}

class TreeBuilder {
    /**
     * @param {string[]} postfix
     * @return {Node}
     */
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

/**
 * @param {string[]} postfix
 * @return {number}
 */
var expTree = function(postfix) {
    return new TreeBuilder().expTree(postfix).evaluate();
};

module.exports = { TreeBuilder, Node, expTree };
