// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    let found = 0;
    const dfs = (node) => {
        if (!node) return null;
        const left = dfs(node.left);
        const right = dfs(node.right);
        if (node === p || node === q) {
            found++;
            return node;
        }
        return left && right ? node : left || right;
    };
    const ans = dfs(root);
    return found === 2 ? ans : null;
};
