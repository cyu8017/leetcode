// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    const canReach = (mid) => {
        let prefix = 0;
        for (let i = 0; i < k; ++i) prefix += nums[i] - mid;
        if (prefix >= 0) return true;
        let prev = 0, minPrev = 0;
        for (let i = k; i < nums.length; ++i) {
            prefix += nums[i] - mid;
            prev += nums[i - k] - mid;
            minPrev = Math.min(minPrev, prev);
            if (prefix - minPrev >= 0) return true;
        }
        return false;
    };
    let left = Math.min(...nums), right = Math.max(...nums);
    for (let i = 0; i < 80; ++i) {
        const mid = (left + right) / 2;
        if (canReach(mid)) left = mid;
        else right = mid;
    }
    return left;
};
