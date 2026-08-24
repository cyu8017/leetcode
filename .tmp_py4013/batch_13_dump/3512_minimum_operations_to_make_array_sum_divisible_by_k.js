// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

var minOperations = function(nums, k) {
    let ans = 0;
    for (const x of nums) ans = (ans + x) % k;
    return ans;
};
