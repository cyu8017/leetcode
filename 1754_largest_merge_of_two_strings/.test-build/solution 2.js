"use strict";
// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/
function largestMerge(word1, word2) {
    let i = 0;
    let j = 0;
    const out = [];
    while (i < word1.length && j < word2.length) {
        if (word1.slice(i) > word2.slice(j)) {
            out.push(word1[i]);
            i++;
        }
        else {
            out.push(word2[j]);
            j++;
        }
    }
    return out.join("") + word1.slice(i) + word2.slice(j);
}
