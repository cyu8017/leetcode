// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    const piles = [];
    for (const num of nums) {
        let left = 0;
        let right = piles.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (piles[mid] < num) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        if (left === piles.length) {
            piles.push(num);
        } else {
            piles[left] = num;
        }
    }
    return piles.length;
};
