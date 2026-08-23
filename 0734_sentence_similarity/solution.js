// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

/**
 * @param {string[]} sentence1
 * @param {string[]} sentence2
 * @param {string[][]} similarPairs
 * @return {boolean}
 */
var areSentencesSimilar = function(sentence1, sentence2, similarPairs) {
    if (sentence1.length !== sentence2.length) return false;
    const pairs = new Set();
    for (const pair of similarPairs) {
        pairs.add(pair[0] + '#' + pair[1]);
        pairs.add(pair[1] + '#' + pair[0]);
    }
    for (let i = 0; i < sentence1.length; i++) {
        if (sentence1[i] !== sentence2[i] && !pairs.has(sentence1[i] + '#' + sentence2[i])) return false;
    }
    return true;
};
