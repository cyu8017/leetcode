// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

export function isBipartite(graph: number[][]): boolean {
    const color = new Array(graph.length).fill(-1);
    const dfs = (node, c) => {
        color[node] = c;
        for (const nei of graph[node]) {
            if (color[nei] === -1) {
                if (!dfs(nei, c ^ 1)) return false;
            } else if (color[nei] === c) {
                return false;
            }
        }
        return true;
    };
    for (let node = 0; node < graph.length; node++) {
        if (color[node] === -1 && !dfs(node, 0)) return false;
    }
    return true;
}
