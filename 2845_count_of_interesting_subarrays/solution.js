// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

/**
 * @param {number[]} nums
 * @param {number} modulo
 * @param {number} k
 * @return {number}
 */
var countInterestingSubarrays = function(nums, modulo, k) {
    const freq = new Map([[0, 1]]);
    let ans = 0, pref = 0;
    for (const v of nums) {
        if (v % modulo === k) pref++;
        let need = (pref - k) % modulo;
        if (need < 0) need += modulo;
        ans += freq.get(need) || 0;
        const key = pref % modulo;
        freq.set(key, (freq.get(key) || 0) + 1);
    }
    return ans;
};
