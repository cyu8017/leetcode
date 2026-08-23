// LeetCode 0357 - Count Numbers with Unique Digits
var countNumbersWithUniqueDigits = function(n) {
    if (n === 0) return 1;

    let total = 10;
    let unique = 9;
    let available = 9;

    for (let length = 2; length <= n; length += 1) {
        unique *= available;
        available -= 1;
        total += unique;
    }

    return total;
};
