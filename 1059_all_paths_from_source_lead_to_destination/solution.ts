// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

function leadsToDestination(n: number, edges: number[][], source: number, destination: number): boolean {
    const graph: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) graph[a].push(b);
    const state = new Array(n).fill(0);

    function dfs(node: number): boolean {
        if (graph[node].length === 0) return node === destination;
        if (state[node] === 1) return false;
        if (state[node] === 2) return true;
        state[node] = 1;
        for (const nxt of graph[node]) {
            if (!dfs(nxt)) return false;
        }
        state[node] = 2;
        return true;
    }

    return dfs(source);
}
