// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var equalToDescendants = function(root) {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return 0;
        const total = dfs(node.left) + dfs(node.right);
        if (total === node.val) ans++;
        return total + node.val;
    };
    dfs(root);
    return ans;
};
