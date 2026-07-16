// LeetCode 0395 - Longest Substring with At Least K Repeating Characters
var longestSubstring = function (s, k) {
    if (!s.length) return 0;

    const counts = new Map();
    for (const char of s) {
        counts.set(char, (counts.get(char) || 0) + 1);
    }

    for (const [char, count] of counts) {
        if (count < k) {
            return Math.max(0, ...s.split(char).map((part) => longestSubstring(part, k)));
        }
    }
    return s.length;
};

module.exports = { longestSubstring };
