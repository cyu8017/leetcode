// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

export function shortestPathLength(graph: number[][]): number {
    const n = graph.length;
    const target = (1 << n) - 1;
    const queue = [];
    const seen = new Set();
    for (let i = 0; i < n; i++) {
        queue.push([i, 1 << i, 0]);
        seen.add((i << 20) | (1 << i));
    }
    while (queue.length) {
        const [node, mask, dist] = queue.shift();
        if (mask === target) return dist;
        for (const nxt of graph[node]) {
            const nmask = mask | (1 << nxt);
            const state = (nxt << 20) | nmask;
            if (!seen.has(state)) {
                seen.add(state);
                queue.push([nxt, nmask, dist + 1]);
            }
        }
    }
    return -1;
}
