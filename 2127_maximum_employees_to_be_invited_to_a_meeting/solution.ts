// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

export function maximumInvitations(favorite: number[]): number {
    const n = favorite.length;
    const indeg = new Array(n).fill(0);
    const depth = new Array(n).fill(1);
    for (const f of favorite) indeg[f]++;
    const q = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) q.push(i);
    while (q.length) {
        const u = q.shift();
        const v = favorite[u];
        depth[v] = Math.max(depth[v], depth[u] + 1);
        if (--indeg[v] === 0) q.push(v);
    }
    let pairSum = 0, maxCycle = 0;
    const vis = new Array(n).fill(false);
    for (let i = 0; i < n; i++) {
        if (indeg[i] === 0 || vis[i]) continue;
        let u = i, lenCycle = 0;
        while (!vis[u]) {
            vis[u] = true;
            u = favorite[u];
            lenCycle++;
        }
        if (lenCycle === 2) pairSum += depth[i] + depth[favorite[i]];
        else maxCycle = Math.max(maxCycle, lenCycle);
    }
    return Math.max(pairSum, maxCycle);
}
