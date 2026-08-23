// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isPossible = function(nums) {
    const freq = new Map();
    const tails = new Map();
    for (const num of nums) freq.set(num, (freq.get(num) || 0) + 1);
    for (const num of nums) {
        if ((freq.get(num) || 0) === 0) continue;
        freq.set(num, freq.get(num) - 1);
        if ((tails.get(num - 1) || 0) > 0) {
            tails.set(num - 1, tails.get(num - 1) - 1);
            tails.set(num, (tails.get(num) || 0) + 1);
        } else if ((freq.get(num + 1) || 0) > 0 && (freq.get(num + 2) || 0) > 0) {
            freq.set(num + 1, freq.get(num + 1) - 1);
            freq.set(num + 2, freq.get(num + 2) - 1);
            tails.set(num + 2, (tails.get(num + 2) || 0) + 1);
        } else {
            return false;
        }
    }
    return true;
};
