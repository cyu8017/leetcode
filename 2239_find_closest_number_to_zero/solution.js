// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function(nums) {
    let ans = nums[0];
    for (const x of nums) {
        if (Math.abs(x) < Math.abs(ans) || (Math.abs(x) === Math.abs(ans) && x > ans)) ans = x;
    }
    return ans;
};
