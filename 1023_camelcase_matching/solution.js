// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

/**
 * @param {string[]} queries
 * @param {string} pattern
 * @return {boolean[]}
 */
var camelMatch = function(queries, pattern) {
    const matches = (q) => {
        let i = 0;
        for (const ch of q) {
            if (i < pattern.length && ch === pattern[i]) i++;
            else if (ch >= 'A' && ch <= 'Z') return false;
        }
        return i === pattern.length;
    };
    return queries.map(matches);
};
