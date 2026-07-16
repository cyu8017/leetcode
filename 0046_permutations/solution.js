// LeetCode 0046 - Permutations
// https://leetcode.com/problems/permutations/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const result = [];
    const path = [];
    const used = new Array(nums.length).fill(false);

    function backtrack() {
        if (path.length === nums.length) {
            result.push(path.slice());
            return;
        }
        for (let i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            used[i] = true;
            path.push(nums[i]);
            backtrack();
            path.pop();
            used[i] = false;
        }
    }

    backtrack();
    return result;
};
