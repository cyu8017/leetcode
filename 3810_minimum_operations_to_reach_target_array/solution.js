// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

var minOperations = function(nums, target) {
    const s = new Set();
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== target[i]) s.add(nums[i]);
    }
    return s.size;
};
