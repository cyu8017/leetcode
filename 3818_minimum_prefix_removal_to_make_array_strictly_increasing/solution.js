// LeetCode 3818 - Minimum Prefix Removal To Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

var minimumPrefixLength = function(nums) {
    for (let i = nums.length - 1; i > 0; i--) {
        if (nums[i - 1] >= nums[i]) return i;
    }
    return 0;
};
