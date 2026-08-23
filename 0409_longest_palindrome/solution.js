// LeetCode 0409 - Longest Palindrome
var longestPalindrome = function (s) {
    const counts = new Map();
    for (const char of s) {
        counts.set(char, (counts.get(char) || 0) + 1);
    }
    let length = 0;
    let odd = false;
    for (const count of counts.values()) {
        length += Math.floor(count / 2) * 2;
        if (count % 2) odd = true;
    }
    return length + (odd ? 1 : 0);
};

module.exports = { longestPalindrome };
