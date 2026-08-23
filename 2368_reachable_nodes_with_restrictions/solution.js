// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} restricted
 * @return {number}
 */
var reachableNodes = function(n, edges, restricted) {
    const ban = new Set(restricted);
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    let ans = 0;
    const vis = Array(n).fill(false);
    const q = [0];
    vis[0] = true;
    while (q.length > 0) {
        const u = q.shift();
        ans++;
        for (const v of g[u]) {
            if (!vis[v] && !ban.has(v)) {
                vis[v] = true;
                q.push(v);
            }
        }
    }
    return ans;
};
