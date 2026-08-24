// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var averageOfSubtree = function(root) {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return [0, 0];
        const L = dfs(node.left);
        const R = dfs(node.right);
        const sum = L[0] + R[0] + node.val;
        const cnt = L[1] + R[1] + 1;
        if (Math.floor(sum / cnt) === node.val) ans++;
        return [sum, cnt];
    };
    dfs(root);
    return ans;
};
