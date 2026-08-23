// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

/**
 * @param {string[]} nums
 * @param {string} target
 * @return {number}
 */
var numOfPairs = function(nums, target) {
    let ans = 0;
    for (let i = 0; i < nums.length; i++)
        for (let j = 0; j < nums.length; j++)
            if (i !== j && nums[i] + nums[j] === target) ans++;
    return ans;
};
