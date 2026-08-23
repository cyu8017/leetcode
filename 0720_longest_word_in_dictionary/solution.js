// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

/**
 * @param {string[]} words
 * @return {string}
 */
var longestWord = function(words) {
    words = words.slice().sort();
    const built = new Set(['']);
    let best = '';
    for (const word of words) {
        if (built.has(word.substring(0, word.length - 1))) {
            built.add(word);
            if (word.length > best.length) best = word;
        }
    }
    return best;
};
