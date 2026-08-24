// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

export function maximumSegmentSum(nums: number[], removeQueries: number[]): number[] {
    const n = nums.length;
    const parent = Array(n);
    const sum = Array(n).fill(0);
    const active = Array(n).fill(false);
    for (let i = 0; i < n; i++) parent[i] = i;
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    const unite = (a, b) => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        parent[rb] = ra;
        sum[ra] += sum[rb];
    };
    const ans = Array(n);
    let best = 0;
    for (let i = n - 1; i >= 0; i--) {
        ans[i] = best;
        const idx = removeQueries[i];
        active[idx] = true;
        sum[idx] = nums[idx];
        if (idx > 0 && active[idx - 1]) unite(idx, idx - 1);
        if (idx + 1 < n && active[idx + 1]) unite(idx, idx + 1);
        best = Math.max(best, sum[find(idx)]);
    }
    return ans;
}
