// LeetCode 0397 - Integer Replacement
var integerReplacement = function (n) {
    let steps = 0;
    while (n !== 1) {
        if (n % 2 === 0) n = Math.floor(n / 2);
        else if (n === 3 || n % 4 === 1) n -= 1;
        else n += 1;
        steps += 1;
    }
    return steps;
};

module.exports = { integerReplacement };
