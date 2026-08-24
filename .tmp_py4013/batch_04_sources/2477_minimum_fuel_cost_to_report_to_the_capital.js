// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

/**
 * @param {number[][]} roads
 * @param {number} seats
 * @return {number}
 */
var minimumFuelCost = function(roads, seats) {
    const n = roads.length + 1;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of roads) {
        g[a].push(b);
        g[b].push(a);
    }
    let ans = 0;
    const dfs = (u, p) => {
        let people = 1;
        for (const v of g[u]) {
            if (v !== p) people += dfs(v, u);
        }
        if (u !== 0) ans += Math.floor((people + seats - 1) / seats);
        return people;
    };
    dfs(0, -1);
    return ans;
};
