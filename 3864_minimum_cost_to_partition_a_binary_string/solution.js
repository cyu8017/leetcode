// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

var minCost = function(s, encCost, flatCost) {
    const n = s.length;
    const pre = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) pre[i] = pre[i - 1] + (s.charCodeAt(i - 1) - 48);
    const dfs = (l, r) => {
        const x = pre[r] - pre[l];
        let res = x !== 0 ? (r - l) * x * encCost : flatCost;
        if ((r - l) % 2 === 0) {
            const m = Math.floor((l + r) / 2);
            res = Math.min(res, dfs(l, m) + dfs(m, r));
        }
        return res;
    };
    return dfs(0, n);
};
