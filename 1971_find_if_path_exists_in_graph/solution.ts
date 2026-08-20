// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

function validPath(n: number, edges: number[][], source: number, destination: number): boolean {
    if (source === destination) return true;
    const g: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const stack: number[] = [source];
    const seen = new Set<number>([source]);
    while (stack.length) {
        const u = stack.pop()!;
        if (u === destination) return true;
        for (const v of g[u]) {
            if (!seen.has(v)) {
                seen.add(v);
                stack.push(v);
            }
        }
    }
    return false;
}
