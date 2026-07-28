// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {string} traversal
 * @return {TreeNode}
 */
var recoverFromPreorder = function(traversal) {
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
        while (i < n && traversal[i] >= '0' && traversal[i] <= '9') i++;
        const node = new TreeNode(Number(traversal.slice(start, i)));
        while (stack.length > depth) stack.pop();
        if (stack.length) {
            if (stack[stack.length - 1].left === null) stack[stack.length - 1].left = node;
            else stack[stack.length - 1].right = node;
        }
        stack.push(node);
    }
    return stack[0];
};
