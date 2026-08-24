// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

function calc3547(left: any, right: any, isCycle: any): any {
    let w0 = right, w1 = right;
    let score = 0;
    for (let value = right - 1; value >= left; value--) {
        score += w0 * value;
        w0 = w1;
        w1 = value;
    }
    if (isCycle) score += w0 * w1;
    return score;
}function getComp(start: any, graph: any, seen: any): any {
    const comp = [start];
    seen[start] = true;
    for (let i = 0; i < comp.length; i++) {
        for (const v of graph[comp[i]]) {
            if (!seen[v]) { seen[v] = true; comp.push(v); }
        }
    }
    return comp;
}export function maxScore(n: any, edges: any): any {
    const graph = Array.from({length: n}, () => []);
    for (const e of edges) {
        graph[e[0]].push(e[1]);
        graph[e[1]].push(e[0]);
    }
    const seen = new Array(n).fill(false);
    const cycleSizes = [], pathSizes = [];
    for (let i = 0; i < n; i++) {
        if (seen[i]) continue;
        const comp = getComp(i, graph, seen);
        let allDeg2 = true;
        for (const u of comp) if (graph[u].length !== 2) { allDeg2 = false; break; }
        if (allDeg2) cycleSizes.push(comp.length);
        else if (comp.length > 1) pathSizes.push(comp.length);
    }
    let ans = 0, curN = n;
    for (const cs of cycleSizes) {
        ans += calc3547(curN - cs + 1, curN, true);
        curN -= cs;
    }
    pathSizes.sort((a, b) => b - a);
    for (const ps of pathSizes) {
        ans += calc3547(curN - ps + 1, curN, false);
        curN -= ps;
    }
    return ans;
}
