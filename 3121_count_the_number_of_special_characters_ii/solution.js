// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    const first = new Array(128).fill(0), last = new Array(128).fill(0);
    for (let i = 0; i < word.length; i++) {
        const c = word.charCodeAt(i);
        if (first[c] === 0) first[c] = i + 1;
        last[c] = i + 1;
    }
    let ans = 0;
    for (let i = 0; i < 26; i++) {
        if (last[97 + i] > 0 && last[97 + i] < first[65 + i]) ans++;
    }
    return ans;
};
