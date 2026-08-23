// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @param {number[]} voyage
 * @return {number[]}
 */
var flipMatchVoyage = function(root, voyage) {
    let i = 0;
    const ans = [];
    const dfs = (node) => {
        if (!node) return true;
        if (node.val !== voyage[i]) return false;
        i++;
        if (node.left && node.left.val !== voyage[i]) {
            ans.push(node.val);
            return dfs(node.right) && dfs(node.left);
        }
        return dfs(node.left) && dfs(node.right);
    };
    return dfs(root) ? ans : [-1];
};
