// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

/**
 * @param {string[]} words
 * @return {number}
 */
var minimumLengthEncoding = function(words) {
    const good = new Set(words);
    for (const word of words) {
        for (let i = 1; i < word.length; i++) good.delete(word.substring(i));
    }
    let ans = 0;
    for (const word of good) ans += word.length + 1;
    return ans;
};
