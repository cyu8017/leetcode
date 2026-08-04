// LeetCode 1328 - Break A Palindrome
// https://leetcode.com/problems/break-a-palindrome/

/**
 * @param {string} palindrome
 * @return {string}
 */
var breakPalindrome = function(palindrome) {
    if (palindrome.length === 1) return "";
    const chars = palindrome.split("");
    for (let i = 0; i < chars.length >> 1; i++) {
        if (chars[i] !== "a") {
            chars[i] = "a";
            return chars.join("");
        }
    }
    chars[chars.length - 1] = "b";
    return chars.join("");
};
