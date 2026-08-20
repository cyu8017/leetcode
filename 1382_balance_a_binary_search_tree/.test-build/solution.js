"use strict";
// LeetCode 1382: Balance A Binary Search Tree
class TreeNode {
    constructor(val, left, right) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}
function balanceBST(root) {
    const values = [];
    const collect = (node) => { if (node) {
        collect(node.left);
        values.push(node.val);
        collect(node.right);
    } };
    const build = (left, right) => {
        if (left > right)
            return null;
        const mid = Math.floor((left + right) / 2);
        const node = new TreeNode(values[mid]);
        node.left = build(left, mid - 1);
        node.right = build(mid + 1, right);
        return node;
    };
    collect(root);
    return build(0, values.length - 1);
}
