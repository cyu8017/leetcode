// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

/**
 * @param {number} n
 * @param {number[][]} roads
 * @param {string[]} names
 * @param {string[]} targetPath
 * @return {number[]}
 */
var mostSimilar = function(n, roads, names, targetPath) {
    const graph = Array.from({ length: n }, () => []);
    for (const [a, b] of roads) {
        graph[a].push(b);
        graph[b].push(a);
    }
    let dp = Array.from({ length: n }, (_, node) => [
        names[node] !== targetPath[0] ? 1 : 0,
        [node]
    ]);
    for (let i = 1; i < targetPath.length; i++) {
        const nextDp = [];
        for (let node = 0; node < n; node++) {
            let bestCost = Infinity, bestPath = null;
            for (const previous of graph[node]) {
                const [cost, path] = dp[previous];
                if (cost < bestCost) {
                    bestCost = cost;
                    bestPath = path;
                }
            }
            nextDp.push([bestCost + (names[node] !== targetPath[i] ? 1 : 0), bestPath.concat(node)]);
        }
        dp = nextDp;
    }
    let best = dp[0];
    for (const item of dp) {
        if (item[0] < best[0]) best = item;
    }
    return best[1];
};
