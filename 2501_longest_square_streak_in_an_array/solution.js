// LeetCode 2501 - Longest Square Streak in an Array
// https://leetcode.com/problems/longest-square-streak-in-an-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSquareStreak = function(nums) {
    const set = new Set(nums.map(Number));
    let best = -1;
    for (const x of nums) {
        if (!set.has(x)) continue;
        let length = 0;
        let cur = x;
        while (set.has(cur)) {
            length++;
            set.delete(cur);
            if (cur > 100000) break;
            cur = cur * cur;
        }
        if (length >= 2 && length > best) best = length;
    }
    return best;
};
