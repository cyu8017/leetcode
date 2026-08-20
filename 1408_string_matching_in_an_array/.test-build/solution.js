"use strict";
// LeetCode 1408: String Matching In An Array
function stringMatching(words) {
    return words.filter((word, i) => words.some((other, j) => i !== j && other.includes(word)));
}
