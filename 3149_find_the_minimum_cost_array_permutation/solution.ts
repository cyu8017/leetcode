// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

export function findPermutation(nums: number[]): number[] {
    const n = nums.length;
    const memo = Array.from({ length: 1 << n }, () => new Array(n).fill(-1));
    const absv = (x) => (x < 0 ? -x : x);
    const dfs = (mask, pre) => {
        if (mask === (1 << n) - 1) return absv(pre - nums[0]);
        if (memo[mask][pre] !== -1) return memo[mask][pre];
        let res = Number.MAX_SAFE_INTEGER;
        for (let cur = 1; cur < n; cur++) {
            if (((mask >> cur) & 1) === 0) {
                res = Math.min(res, absv(pre - nums[cur]) + dfs(mask | (1 << cur), cur));
            }
        }
        return memo[mask][pre] = res;
    };
    const ans = [];
    const g = (mask, pre) => {
        ans.push(pre);
        if (mask === (1 << n) - 1) return;
        const res = dfs(mask, pre);
        for (let cur = 1; cur < n; cur++) {
            if (((mask >> cur) & 1) === 0) {
                if (absv(pre - nums[cur]) + dfs(mask | (1 << cur), cur) === res) {
                    g(mask | (1 << cur), cur);
                    break;
                }
            }
        }
    };
    g(1, 0);
    return ans;
}
