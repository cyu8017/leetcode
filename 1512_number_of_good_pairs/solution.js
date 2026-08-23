// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    const count = new Map();
    let ans = 0;
    for (const n of nums) {
        const c = count.get(n) || 0;
        ans += c;
        count.set(n, c + 1);
    }
    return ans;
};
