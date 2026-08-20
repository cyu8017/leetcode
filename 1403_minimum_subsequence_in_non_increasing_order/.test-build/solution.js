"use strict";
// LeetCode 1403: Minimum Subsequence In Non Increasing Order
function minSubsequence(nums) {
    nums.sort((a, b) => b - a);
    const total = nums.reduce((sum, value) => sum + value, 0), result = [];
    let selected = 0;
    for (const value of nums) {
        selected += value;
        result.push(value);
        if (selected > total - selected)
            break;
    }
    return result;
}
