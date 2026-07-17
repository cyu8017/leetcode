// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    const vowels = new Set('aeiouAEIOU');
    const mid = s.length / 2;
    let balance = 0;
    for (let i = 0; i < s.length; i++) {
        if (vowels.has(s[i])) {
            balance += i < mid ? 1 : -1;
        }
    }
    return balance === 0;
};
