// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var missingElement = function(nums, k) {
    const missing = (i) => nums[i] - nums[0] - i;
    const n = nums.length;
    if (k > missing(n - 1)) return nums[n - 1] + k - missing(n - 1);
    let lo = 0;
    let hi = n - 1;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (missing(mid) < k) lo = mid + 1;
        else hi = mid;
    }
    return nums[lo - 1] + k - missing(lo - 1);
};
