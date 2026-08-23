// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

/**
 * @param {number[]} nums
 * @param {number} cost1
 * @param {number} cost2
 * @return {number}
 */
var minCostToEqualizeArray = function(nums, cost1, cost2) {
    const MOD = 1000000007;
    const n = nums.length;
    let minNum = nums[0], maxNum = nums[0], sum = 0;
    for (const v of nums) {
        minNum = Math.min(minNum, v);
        maxNum = Math.max(maxNum, v);
        sum += v;
    }
    if (cost1 * 2 <= cost2 || n < 3) {
        const totalGap = maxNum * n - sum;
        return Number((BigInt(cost1) * BigInt(totalGap)) % BigInt(MOD));
    }
    let ans = Number.MAX_SAFE_INTEGER;
    for (let target = maxNum; target < 2 * maxNum; target++) {
        const maxGap = target - minNum;
        const totalGap = target * n - sum;
        let pairs = Math.floor(totalGap / 2);
        const alt = totalGap - maxGap;
        if (alt < pairs) pairs = alt;
        const cost = cost1 * (totalGap - 2 * pairs) + cost2 * pairs;
        ans = Math.min(ans, cost);
    }
    return ans % MOD;
};
