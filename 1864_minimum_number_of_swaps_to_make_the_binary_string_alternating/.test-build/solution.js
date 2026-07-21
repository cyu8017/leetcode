"use strict";
// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
function minSwaps(s) {
    let zeros = 0;
    for (const ch of s)
        if (ch === "0")
            zeros++;
    const ones = s.length - zeros;
    if (Math.abs(zeros - ones) > 1)
        return -1;
    const mismatches = (pattern) => {
        let count = 0;
        for (let i = 0; i < s.length; i++) {
            if (s[i] !== pattern[i % 2])
                count++;
        }
        return count >> 1;
    };
    if (zeros === ones)
        return Math.min(mismatches("01"), mismatches("10"));
    if (zeros > ones)
        return mismatches("01");
    return mismatches("10");
}
