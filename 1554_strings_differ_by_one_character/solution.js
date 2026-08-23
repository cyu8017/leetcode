// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

/**
 * @param {string[]} dict
 * @return {boolean}
 */
var differByOne = function(dict) {
    const seen = new Set();
    for (const word of dict) {
        for (let i = 0; i < word.length; i++) {
            const pattern = word.slice(0, i) + "*" + word.slice(i + 1);
            if (seen.has(pattern)) return true;
            seen.add(pattern);
        }
    }
    return false;
};
