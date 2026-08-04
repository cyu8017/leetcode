// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

/**
 * @param {string} s
 * @return {number}
 */
var countLetters = function(s) {
    let ans = 1, length = 1;
    for (let i = 1; i < s.length; i++) {
        length = s[i] === s[i - 1] ? length + 1 : 1;
        ans += length;
    }
    return ans;
};
