// LeetCode 0400 - Nth Digit
var findNthDigit = function (n) {
    let digits = 1;
    let count = 9;
    let start = 1;

    while (n > digits * count) {
        n -= digits * count;
        digits += 1;
        count *= 10;
        start *= 10;
    }

    const number = start + Math.floor((n - 1) / digits);
    return Number(String(number)[(n - 1) % digits]);
};

module.exports = { findNthDigit };
