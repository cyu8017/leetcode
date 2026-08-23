// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

var missingInteger = function(nums) {
    let sum = nums[0];
    for (let i = 1; i < nums.length && nums[i] === nums[i - 1] + 1; i++) {
        sum += nums[i];
    }
    const seen = new Set(nums);
    while (seen.has(sum)) sum++;
    return sum;
};
