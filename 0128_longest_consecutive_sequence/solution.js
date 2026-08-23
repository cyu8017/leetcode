// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const values = new Set(nums);
    let best = 0;

    for (const num of values) {
        if (values.has(num - 1)) {
            continue;
        }
        let length = 1;
        while (values.has(num + length)) {
            length++;
        }
        best = Math.max(best, length);
    }

    return best;
};