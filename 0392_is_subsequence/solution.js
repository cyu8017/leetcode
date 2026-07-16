// LeetCode 0392 - Is Subsequence
var isSubsequence = function (s, t) {
    let index = 0;
    for (const char of t) {
        if (index < s.length && s[index] === char) index += 1;
    }
    return index === s.length;
};

module.exports = { isSubsequence };
