var minTime = function(n, edges, hasApple) {
    const graph = Array.from({length: n}, () => []); for (const [a, b] of edges) { graph[a].push(b); graph[b].push(a); }
    const dfs = (node, parent) => { let time = 0; for (const child of graph[node]) if (child !== parent) { const childTime = dfs(child, node); if (childTime || hasApple[child]) time += childTime + 2; } return time; };
    return dfs(0, -1);
};
