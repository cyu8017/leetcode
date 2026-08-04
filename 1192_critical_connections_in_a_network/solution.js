// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number[][]}
 */
var criticalConnections = function(n, connections) {
    const graph = Array.from({ length: n }, () => []);
    for (const [a, b] of connections) {
        graph[a].push(b);
        graph[b].push(a);
    }
    const disc = Array(n).fill(-1);
    const low = Array(n).fill(-1);
    let time = 0;
    const bridges = [];
    const dfs = (node, parent) => {
        disc[node] = low[node] = time++;
        for (const nxt of graph[node]) {
            if (nxt === parent) continue;
            if (disc[nxt] === -1) {
                dfs(nxt, node);
                low[node] = Math.min(low[node], low[nxt]);
                if (low[nxt] > disc[node]) bridges.push([Math.min(node, nxt), Math.max(node, nxt)]);
            } else {
                low[node] = Math.min(low[node], disc[nxt]);
            }
        }
    };
    dfs(0, -1);
    return bridges;
};
