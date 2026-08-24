// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minSwaps = function(nums) {
    let ones = 0;
    for (const x of nums) ones += x;
    if (ones === 0) return 0;
    const n = nums.length;
    let window = 0;
    for (let i = 0; i < ones; i++) window += nums[i];
    let best = window;
    for (let i = 0; i < n; i++) {
        window -= nums[i];
        window += nums[(i + ones) % n];
        best = Math.max(best, window);
    }
    return ones - best;
};
