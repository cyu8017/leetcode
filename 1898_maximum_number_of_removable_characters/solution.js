// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

/**
 * @param {string} s
 * @param {string} p
 * @param {number[]} removable
 * @return {number}
 */
var maximumRemovals = function(s, p, removable) {
    const stillSubsequence = (k) => {
        const removed = new Set(removable.slice(0, k));
        let index = 0;
        for (let position = 0; position < s.length; position++) {
            if (removed.has(position)) continue;
            if (index < p.length && s[position] === p[index]) index++;
        }
        return index === p.length;
    };
    let lo = 0, hi = removable.length;
    while (lo < hi) {
        const mid = (lo + hi + 1) >> 1;
        if (stillSubsequence(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
