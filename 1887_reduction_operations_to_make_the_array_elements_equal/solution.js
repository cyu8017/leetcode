// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

/**
 * @param {number[]} nums
 * @return {number}
 */
var reductionOperations = function(nums) {
    nums = nums.slice().sort((a, b) => a - b);
    let answer = 0, rank = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i - 1]) rank++;
        answer += rank;
    }
    return answer;
};
