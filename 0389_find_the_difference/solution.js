// LeetCode 0389 - Find the Difference
var findTheDifference = function (s, t) {
    let xorValue = 0;
    for (const char of s + t) {
        xorValue ^= char.charCodeAt(0);
    }
    return String.fromCharCode(xorValue);
};

module.exports = { findTheDifference };
