// LeetCode 3908 - Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/

var validDigit = function(n, x) {
    let hasX = false;
    while (n > 9) {
        hasX = hasX || (n % 10 === x);
        n = Math.floor(n / 10);
    }
    return hasX && (n !== x);
};
