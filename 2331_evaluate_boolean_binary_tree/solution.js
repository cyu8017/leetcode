// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var evaluateTree = function(root) {
    if (root.left === null && root.right === null) return root.val === 1;
    const l = evaluateTree(root.left);
    const r = evaluateTree(root.right);
    if (root.val === 2) return l || r;
    return l && r;
};
