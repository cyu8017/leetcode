function minTime(n: any, edges: any, hasApple: any): any {
    const graph = Array.from({length: n}, (: any): any => []); for (const [a, b] of edges) { graph[a].push(b); graph[b].push(a); }
    const dfs = (node: any, parent: any): any => { let time = 0; for (const child of graph[node]) if (child !== parent) { const childTime = dfs(child, node); if (childTime || hasApple[child]) time += childTime + 2; } return time; };
    return dfs(0, -1);
}
