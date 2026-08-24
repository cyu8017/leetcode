// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumAverageDifference = function(nums) {
    const n = nums.length;
    let total = 0;
    for (const v of nums) total += v;
    let left = 0, bestDiff = Infinity, bestIdx = 0;
    for (let i = 0; i < n; i++) {
        left += nums[i];
        const leftAvg = Math.floor(left / (i + 1));
        let rightAvg = 0;
        if (i !== n - 1) rightAvg = Math.floor((total - left) / (n - i - 1));
        const diff = Math.abs(leftAvg - rightAvg);
        if (diff < bestDiff) { bestDiff = diff; bestIdx = i; }
    }
    return bestIdx;
};
