// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

function leftDepth(node) {
    let depth = 0;
    while (node) {
        depth += 1;
        node = node.left;
    }
    return depth;
}

function rightDepth(node) {
    let depth = 0;
    while (node) {
        depth += 1;
        node = node.right;
    }
    return depth;
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var countNodes = function(root) {
    if (!root) {
        return 0;
    }
    const left = leftDepth(root);
    const right = rightDepth(root);
    if (left === right) {
        return (1 << left) - 1;
    }
    return 1 + countNodes(root.left) + countNodes(root.right);
};
