// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

/**
 * @param {string} word
 * @return {number}
 */
var countVowels = function(word) {
    const isVowel = (c) => "aeiou".includes(c);
    const n = word.length;
    let ans = 0;
    for (let i = 0; i < n; i++)
        if (isVowel(word[i])) ans += (i + 1) * (n - i);
    return ans;
};
