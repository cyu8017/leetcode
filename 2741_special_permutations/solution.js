// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

/**
 * @param {number[]} nums
 * @return {number}
 */
var specialPerm = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;
    const memo = Array.from({length: 1 << n}, () => Array(n).fill(-1));
    const dfs = (mask, last) => {
        if (mask === (1 << n) - 1) return 1;
        if (memo[mask][last] !== -1) return memo[mask][last];
        let res = 0;
        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;
            if (nums[i] % nums[last] === 0 || nums[last] % nums[i] === 0)
                res = (res + dfs(mask | (1 << i), i)) % MOD;
        }
        return memo[mask][last] = res;
    };
    let ans = 0;
    for (let i = 0; i < n; i++) ans = (ans + dfs(1 << i, i)) % MOD;
    return ans;
};
