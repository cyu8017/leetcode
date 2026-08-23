// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

var maxSum = function(root) {
    const g = new Map();
    const vis = new Map();
    const dfs = (node, p) => {
        if (!node) return;
        g.set(node, [p, node.left, node.right]);
        dfs(node.left, node);
        dfs(node.right, node);
    };
    const dfs2 = (node) => {
        if (!node || vis.get(node.val) === true) return 0;
        vis.set(node.val, true);
        const res = node.val;
        let best = 0;
        for (const nxt of g.get(node)) best = Math.max(best, dfs2(nxt));
        vis.set(node.val, false);
        return res + best;
    };
    g.clear();
    vis.clear();
    dfs(root, null);
    let ans = -Infinity;
    for (const node of g.keys()) {
        ans = Math.max(ans, dfs2(node));
        vis.clear();
    }
    return ans;
};
