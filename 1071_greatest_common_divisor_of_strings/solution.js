// LeetCode 1071 - Greatest Common Divisor of Strings
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    if (str1 + str2 !== str2 + str1) return "";
    function gcd(a, b) {
        while (b) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
    return str1.slice(0, gcd(str1.length, str2.length));
};
