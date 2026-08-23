// LeetCode 0390 - Elimination Game
var lastRemaining = function (n) {
    let left = 1;
    let right = n;
    let step = 1;
    let remaining = n;
    let fromLeft = true;

    while (left < right) {
        if (fromLeft || remaining % 2 === 1) left += step;
        right -= step;
        step *= 2;
        remaining = Math.floor(remaining / 2);
        fromLeft = !fromLeft;
    }

    return left;
};

module.exports = { lastRemaining };
