// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

export function longestSpecialPath(edges: any, nums: any): any {
    const n = nums.length;
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    let bestLen = 0, bestNodes = 1;
    const last = new Map();
    const path = [];
    const dfs = (u, p, dist, left) => {
        const seen = last.has(nums[u]);
        const prevPos = seen ? last.get(nums[u]) : -1;
        last.set(nums[u], path.length);
        let newLeft = left;
        if (seen && prevPos >= left) newLeft = prevPos + 1;
        path.push(dist);
        const length = dist - path[newLeft];
        const nodes = path.length - newLeft;
        if (length > bestLen || (length === bestLen && nodes < bestNodes)) {
            bestLen = length;
            bestNodes = nodes;
        }
        for (const e of g[u]) {
            if (e[0] === p) continue;
            dfs(e[0], u, dist + e[1], newLeft);
        }
        path.pop();
        if (seen) last.set(nums[u], prevPos);
        else last.delete(nums[u]);
    };
    dfs(0, -1, 0, 0);
    return [bestLen, bestNodes];
}
