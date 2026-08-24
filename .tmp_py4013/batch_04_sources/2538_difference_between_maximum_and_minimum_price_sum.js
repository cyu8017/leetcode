// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} price
 * @return {number}
 */
var maxOutput = function(n, edges, price) {
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    let ans = 0;
    const dfs = (u, p) => {
        let maxChild = 0;
        for (const v of g[u]) {
            if (v === p) continue;
            const child = dfs(v, u);
            if (child > maxChild) maxChild = child;
            if (child > ans) ans = child;
        }
        return price[u] + maxChild;
    };
    dfs(0, -1);
    return ans;
};
