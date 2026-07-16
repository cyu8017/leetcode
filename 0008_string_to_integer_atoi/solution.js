// LeetCode 0008 - String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let i = 0;
    while (i < s.length && s[i] === " ") {
        i++;
    }
    if (i >= s.length) {
        return 0;
    }

    let sign = 1;
    if (s[i] === "-") {
        sign = -1;
        i++;
    } else if (s[i] === "+") {
        i++;
    }

    let result = 0;
    while (i < s.length && s[i] >= "0" && s[i] <= "9") {
        const digit = s.charCodeAt(i) - "0".charCodeAt(0);
        if (result > (2147483647 - digit) / 10) {
            return sign === -1 ? -2147483648 : 2147483647;
        }
        result = result * 10 + digit;
        i++;
    }

    return sign * result;
};
