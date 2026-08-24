// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

export function componentValue(nums: number[], edges: number[][]): number {
    const n = nums.length;
    let total = 0;
    for (const x of nums) total += x;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const dfs = (u, p, target) => {
        let sum = nums[u];
        for (const v of g[u]) {
            if (v === p) continue;
            const sub = dfs(v, u, target);
            if (sub < 0) return -1;
            sum += sub;
        }
        if (sum > target) return -1;
        if (sum === target) return 0;
        return sum;
    };
    for (let parts = n; parts >= 1; parts--) {
        if (total % parts !== 0) continue;
        const target = total / parts;
        if (dfs(0, -1, target) === 0) return parts - 1;
    }
    return 0;
}
