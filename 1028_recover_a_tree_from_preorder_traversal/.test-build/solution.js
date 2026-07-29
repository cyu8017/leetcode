"use strict";
// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
function recoverFromPreorder(traversal) {
    const stack = [];
    let i = 0;
    const n = traversal.length;
    while (i < n) {
        let depth = 0;
        while (i < n && traversal[i] === '-') {
            depth++;
            i++;
        }
        let start = i;
        while (i < n && traversal[i] >= '0' && traversal[i] <= '9')
            i++;
        const node = new TreeNode(Number(traversal.slice(start, i)));
        while (stack.length > depth)
            stack.pop();
        if (stack.length) {
            const parent = stack[stack.length - 1];
            if (parent.left === null)
                parent.left = node;
            else
                parent.right = node;
        }
        stack.push(node);
    }
    return stack[0] ?? null;
}
