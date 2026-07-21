// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countNicePairs = function(nums) {
    const MOD = 1e9 + 7;
    const rev = (x) => Number(String(x).split('').reverse().join(''));
    const freq = new Map();
    let ans = 0;
    for (const num of nums) {
        const diff = num - rev(num);
        ans = (ans + (freq.get(diff) || 0)) % MOD;
        freq.set(diff, (freq.get(diff) || 0) + 1);
    }
    return ans;
};
