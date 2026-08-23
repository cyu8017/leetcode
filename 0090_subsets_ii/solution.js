// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums.sort((a, b) => a - b);
    const result = [];

    function backtrack(start, path) {
        result.push(path.slice());
        for (let i = start; i < nums.length; i++) {
            if (i > start && nums[i] === nums[i - 1]) {
                continue;
            }
            path.push(nums[i]);
            backtrack(i + 1, path);
            path.pop();
        }
    }

    backtrack(0, []);
    return result;
};
