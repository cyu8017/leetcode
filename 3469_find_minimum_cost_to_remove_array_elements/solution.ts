// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

export function minCost(nums: any): any {
    const n = nums.length;
    const memo = new Map();
    const max2 = (a, b) => (a > b ? a : b);
    const min3 = (a, b, c) => Math.min(a, Math.min(b, c));
    const key = (i, prev) => (BigInt(i) << 32n) | BigInt(prev >>> 0);
    const dfs = (i, prev) => {
        if (i >= n) return prev === -1 ? 0 : nums[prev];
        const k = key(i, prev).toString();
        if (memo.has(k)) return memo.get(k);
        let res;
        if (prev === -1) {
            if (i + 1 >= n) res = nums[i];
            else if (i + 2 >= n) res = max2(nums[i], nums[i + 1]);
            else {
                const a = nums[i], b = nums[i + 1], c = nums[i + 2];
                res = min3(max2(b, c) + dfs(i + 3, i), max2(a, c) + dfs(i + 3, i + 1), max2(a, b) + dfs(i + 3, i + 2));
            }
        } else {
            if (i + 1 >= n) res = max2(nums[prev], nums[i]);
            else {
                const a = nums[prev], b = nums[i], c = nums[i + 1];
                res = min3(max2(b, c) + dfs(i + 2, prev), max2(a, c) + dfs(i + 2, i), max2(a, b) + dfs(i + 2, i + 1));
            }
        }
        memo.set(k, res);
        return res;
    };
    return dfs(0, -1);
}
