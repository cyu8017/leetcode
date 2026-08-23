// LeetCode 2366 - Minimum Replacements to Sort the Array
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumReplacement = function(nums) {
    let ans = 0;
    const n = nums.length;
    let prev = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] <= prev) { prev = nums[i]; continue; }
        const parts = Math.floor((nums[i] + prev - 1) / prev);
        ans += parts - 1;
        prev = Math.floor(nums[i] / parts);
    }
    return ans;
};
