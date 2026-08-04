// LeetCode 1372 - Longest Zigzag Path In A Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var longestZigZag = function(root) {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return [-1, -1];
        const l = dfs(node.left), r = dfs(node.right);
        const a = l[1] + 1, b = r[0] + 1;
        ans = Math.max(ans, a, b);
        return [a, b];
    };
    dfs(root);
    return ans;
};
