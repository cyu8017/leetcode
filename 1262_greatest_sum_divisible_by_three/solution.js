// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSumDivThree = function(nums) {
    const impossible = -1e18;
    const dp = [0, impossible, impossible];
    for (const value of nums) {
        const old = dp.slice();
        for (let total = 0; total < 3; total++) {
            if (old[total] !== impossible) {
                const remainder = (old[total] + value) % 3;
                dp[remainder] = Math.max(dp[remainder], old[total] + value);
            }
        }
    }
    return dp[0];
};
