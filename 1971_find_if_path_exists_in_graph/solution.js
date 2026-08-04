// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function(n, edges, source, destination) {
    if (source === destination) return true;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const stack = [source];
    const seen = new Set([source]);
    while (stack.length) {
        const u = stack.pop();
        if (u === destination) return true;
        for (const v of g[u]) {
            if (!seen.has(v)) {
                seen.add(v);
                stack.push(v);
            }
        }
    }
    return false;
};
