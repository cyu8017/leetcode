// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

class Solution {
    frequencySort(s) {
        const counts = new Map();
        for (const char of s) {
            counts.set(char, (counts.get(char) || 0) + 1);
        }
        const ordered = [...counts.entries()].sort(
            (a, b) => b[1] - a[1] || a[0].codePointAt(0) - b[0].codePointAt(0),
        );
        return ordered.map(([char, count]) => char.repeat(count)).join("");
    }
}

module.exports = { Solution };
