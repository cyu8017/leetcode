// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    const n = nums.length;
    const seen = Array(n + 1).fill(0);
    let duplicate = -1, missing = -1;
    for (const value of nums) ++seen[value];
    for (let value = 1; value <= n; ++value) {
        if (seen[value] === 2) duplicate = value;
        else if (seen[value] === 0) missing = value;
    }
    return [duplicate, missing];
};
