"use strict";
// LeetCode 1371 - Find The Longest Substring Containing Vowels In Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
function findTheLongestSubstring(s) {
    const first = new Map([[0, -1]]);
    let mask = 0, ans = 0;
    const vowels = "aeiou";
    for (let i = 0; i < s.length; i++) {
        const idx = vowels.indexOf(s[i]);
        if (idx >= 0)
            mask ^= 1 << idx;
        if (first.has(mask))
            ans = Math.max(ans, i - first.get(mask));
        else
            first.set(mask, i);
    }
    return ans;
}
