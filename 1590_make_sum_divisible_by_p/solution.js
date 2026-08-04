// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minSubarray = function(nums, p) {
    let total = 0;
    for (const x of nums) total += x;
    const target = total % p;
    if (target === 0) return 0;
    const seen = new Map([[0, -1]]);
    let prefix = 0, answer = nums.length;
    for (let i = 0; i < nums.length; i++) {
        prefix = (prefix + nums[i]) % p;
        const need = (prefix - target + p) % p;
        if (seen.has(need)) answer = Math.min(answer, i - seen.get(need));
        seen.set(prefix, i);
    }
    return answer < nums.length ? answer : -1;
};
