// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    const s = new Array(128).fill(false);
    for (let i = 0; i < word.length; i++) s[word.charCodeAt(i)] = true;
    let ans = 0;
    for (let i = 0; i < 26; i++) {
        if (s[97 + i] && s[65 + i]) ans++;
    }
    return ans;
};
