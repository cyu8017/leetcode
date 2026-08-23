// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumberOfLIS = function(nums) {
    const n = nums.length;
    const lengths = Array(n).fill(1);
    const counts = Array(n).fill(1);
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < i; ++j) {
            if (nums[j] >= nums[i]) continue;
            if (lengths[j] + 1 > lengths[i]) {
                lengths[i] = lengths[j] + 1;
                counts[i] = counts[j];
            } else if (lengths[j] + 1 === lengths[i]) {
                counts[i] += counts[j];
            }
        }
    }
    let longest = 0;
    for (const length of lengths) longest = Math.max(longest, length);
    let answer = 0;
    for (let i = 0; i < n; ++i) if (lengths[i] === longest) answer += counts[i];
    return answer;
};
