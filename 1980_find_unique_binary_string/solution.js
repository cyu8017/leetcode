// LeetCode 1980 - Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/

/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    const s = new Set(nums);
    const n = nums.length;
    const preferred = ["11", "101", "00", "10", "01", "000", "001", "010", "011", "100", "110", "111"];
    for (const cand of preferred) {
        if (cand.length === n && !s.has(cand)) return cand;
    }
    for (let i = 0; i < (1 << n); i++) {
        const cand = i.toString(2).padStart(n, "0");
        if (!s.has(cand)) return cand;
    }
    return "0".repeat(n);
};
