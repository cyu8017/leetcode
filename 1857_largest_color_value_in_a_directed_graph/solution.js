// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

/**
 * @param {string} colors
 * @param {number[][]} edges
 * @return {number}
 */
var largestPathValue = function(colors, edges) {
    const n = colors.length;
    const indegree = new Array(n).fill(0);
    const adjacency = Array.from({ length: n }, () => []);
    for (const [from, to] of edges) {
        adjacency[from].push(to);
        indegree[to]++;
    }
    const queue = [];
    for (let i = 0; i < n; i++) if (indegree[i] === 0) queue.push(i);
    const dp = Array.from({ length: n }, () => new Array(26).fill(0));
    for (let i = 0; i < n; i++) dp[i][colors.charCodeAt(i) - 97] = 1;

    let processed = 0, answer = 0, head = 0;
    while (head < queue.length) {
        const node = queue[head++];
        processed++;
        answer = Math.max(answer, Math.max(...dp[node]));
        for (const neighbor of adjacency[node]) {
            const neighborColor = colors.charCodeAt(neighbor) - 97;
            for (let c = 0; c < 26; c++) {
                let candidate = dp[node][c];
                if (c === neighborColor) candidate++;
                if (candidate > dp[neighbor][c]) dp[neighbor][c] = candidate;
            }
            indegree[neighbor]--;
            if (indegree[neighbor] === 0) queue.push(neighbor);
        }
    }
    return processed === n ? answer : -1;
};
