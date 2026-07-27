// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

function maximalNetworkRank(n: number, roads: number[][]): number {
    const degree = Array(n).fill(0);
    const edges = new Set<string>();
    for (const [a, b] of roads) {
        degree[a]++;
        degree[b]++;
        edges.add(`${Math.min(a, b)},${Math.max(a, b)}`);
    }
    let ans = 0;
    for (let a = 0; a < n; a++) {
        for (let b = a + 1; b < n; b++) {
            ans = Math.max(ans, degree[a] + degree[b] - (edges.has(`${a},${b}`) ? 1 : 0));
        }
    }
    return ans;
}
