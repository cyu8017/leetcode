"use strict";
// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/
function truncateSentence(s, k) {
    return s.split(' ').slice(0, k).join(' ');
}
