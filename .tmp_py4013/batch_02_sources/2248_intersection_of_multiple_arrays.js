// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var intersection = function(nums) {
    const freq = new Map();
    for (const arr of nums) {
        const seen = new Set();
        for (const x of arr) {
            if (!seen.has(x)) {
                seen.add(x);
                freq.set(x, (freq.get(x) || 0) + 1);
            }
        }
    }
    const ans = [];
    for (const [k, v] of freq) if (v === nums.length) ans.push(k);
    ans.sort((a, b) => a - b);
    return ans;
};
