// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution {
    findAnagrams(s, p) {
        if (p.length > s.length) return [];

        const need = new Array(26).fill(0);
        const window = new Array(26).fill(0);
        for (const char of p) {
            need[char.charCodeAt(0) - 97] += 1;
        }

        const result = [];
        let left = 0;
        for (let right = 0; right < s.length; right += 1) {
            window[s.charCodeAt(right) - 97] += 1;
            if (right - left + 1 > p.length) {
                window[s.charCodeAt(left) - 97] -= 1;
                left += 1;
            }
            if (window.every((count, index) => count === need[index])) {
                result.push(left);
            }
        }
        return result;
    }
}

module.exports = { Solution };
