// LeetCode 0387 - First Unique Character in a String
var firstUniqChar = function (s) {
    const counts = new Map();
    for (const char of s) {
        counts.set(char, (counts.get(char) || 0) + 1);
    }
    for (let index = 0; index < s.length; index += 1) {
        if (counts.get(s[index]) === 1) return index;
    }
    return -1;
};

module.exports = { firstUniqChar };
