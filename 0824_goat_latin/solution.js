// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

/**
 * @param {string} sentence
 * @return {string}
 */
var toGoatLatin = function(sentence) {
    const vowels = new Set(['a','e','i','o','u','A','E','I','O','U']);
    const words = sentence.split(' ');
    const result = [];
    for (let i = 0; i < words.length; i++) {
        let w = words[i];
        if (vowels.has(w[0])) w = w + "ma";
        else w = w.substring(1) + w[0] + "ma";
        w += "a".repeat(i + 1);
        result.push(w);
    }
    return result.join(' ');
};
