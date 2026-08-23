// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var sumOfPowers = function(nums, k) {
    const MOD = 1000000007;
    nums = nums.slice().sort((a, b) => a - b);
    const n = nums.length;
    const f = new Map();
    const dfs = (i, j, kk, mi) => {
        if (i >= n) return kk === 0 ? mi : 0;
        if (n - i < kk) return 0;
        const key = (BigInt(mi) << 18n) | (BigInt(i) << 12n) | (BigInt(j) << 6n) | BigInt(kk);
        const keyS = key.toString();
        if (f.has(keyS)) return f.get(keyS);
        let ans = dfs(i + 1, j, kk, mi);
        if (j === n) ans = (ans + dfs(i + 1, i, kk - 1, mi)) % MOD;
        else ans = (ans + dfs(i + 1, i, kk - 1, Math.min(mi, nums[i] - nums[j]))) % MOD;
        f.set(keyS, ans);
        return ans;
    };
    return dfs(0, n, k, Number.MAX_SAFE_INTEGER);
};
