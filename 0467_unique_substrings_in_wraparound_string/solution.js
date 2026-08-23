// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

class Solution {
    findSubstringInWraproundString(s) {
        const counts = new Array(26).fill(0);
        let length = 0;
        for (let index = 0; index < s.length; index += 1) {
            const char = s[index];
            if (index > 0 && (char.charCodeAt(0) - s.charCodeAt(index - 1) + 26) % 26 === 1) {
                length += 1;
            } else {
                length = 1;
            }
            const position = char.charCodeAt(0) - "a".charCodeAt(0);
            counts[position] = Math.max(counts[position], length);
        }
        return counts.reduce((total, value) => total + value, 0);
    }
}

module.exports = { Solution };
