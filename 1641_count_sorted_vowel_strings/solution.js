// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

/**
 * @param {number} n
 * @return {number}
 */
var countVowelStrings = function(n) {
    const comb = (N, R) => {
        let num = 1, den = 1;
        for (let i = 0; i < R; i++) {
            num *= N - i;
            den *= i + 1;
        }
        return num / den;
    };
    return comb(n + 4, 4);
};
