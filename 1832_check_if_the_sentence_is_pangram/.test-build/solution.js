"use strict";
// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/
function checkIfPangram(sentence) {
    return new Set(sentence).size === 26;
}
