// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

/**
 * @param {string} sentence
 * @return {boolean}
 */
var isCircularSentence = function(sentence) {
    const n = sentence.length;
    if (sentence[0] !== sentence[n - 1]) return false;
    for (let i = 0; i < n; i++) {
        if (sentence[i] === ' ' && sentence[i - 1] !== sentence[i + 1]) return false;
    }
    return true;
};
