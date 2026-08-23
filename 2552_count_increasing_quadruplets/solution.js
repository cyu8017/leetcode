// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    const n = nums.length;
    let ans = 0;
    const great = new Array(n).fill(0);
    for (let j = 0; j < n; ++j) {
        for (let i = 0; i < j; ++i) {
            if (nums[i] < nums[j]) ans += great[i];
            else if (nums[i] > nums[j]) great[i]++;
        }
    }
    return ans;
};
