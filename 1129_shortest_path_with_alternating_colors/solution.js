// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

/**
 * @param {number} n
 * @param {number[][]} redEdges
 * @param {number[][]} blueEdges
 * @return {number[]}
 */
var shortestAlternatingPaths = function(n, redEdges, blueEdges) {
    const graph = [Array.from({ length: n }, () => []), Array.from({ length: n }, () => [])];
    for (const [u, v] of redEdges) graph[0][u].push(v);
    for (const [u, v] of blueEdges) graph[1][u].push(v);
    const ans = Array(n).fill(-1);
    const queue = [[0, 0, 0], [0, 1, 0]];
    const seen = new Set(["0,0", "0,1"]);
    let qi = 0;
    while (qi < queue.length) {
        const [node, color, dist] = queue[qi++];
        if (ans[node] === -1) ans[node] = dist;
        const nextColor = 1 - color;
        for (const nxt of graph[color][node]) {
            const key = `${nxt},${nextColor}`;
            if (!seen.has(key)) {
                seen.add(key);
                queue.push([nxt, nextColor, dist + 1]);
            }
        }
    }
    return ans;
};
