// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

/**
 * @param {string} a
 * @param {string} b
 * @return {boolean}
 */
var checkPalindromeFormation = function(a, b) {
    const isPal = (s) => {
        let i = 0, j = s.length - 1;
        while (i < j) {
            if (s[i++] !== s[j--]) return false;
        }
        return true;
    };
    const check = (x, y) => {
        let i = 0, j = x.length - 1;
        while (i < j && x[i] === y[j]) {
            i++;
            j--;
        }
        return isPal(x.slice(i, j + 1)) || isPal(y.slice(i, j + 1));
    };
    return check(a, b) || check(b, a);
};
