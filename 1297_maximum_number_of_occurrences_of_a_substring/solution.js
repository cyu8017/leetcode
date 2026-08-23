// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

/**
 * @param {string} s
 * @param {number} maxLetters
 * @param {number} minSize
 * @param {number} maxSize
 * @return {number}
 */
var maxFreq = function(s, maxLetters, minSize, maxSize) {
    const counts = new Map();
    for (let i = 0; i + minSize <= s.length; i++) {
        const sub = s.slice(i, i + minSize);
        if (new Set(sub).size <= maxLetters) {
            counts.set(sub, (counts.get(sub) || 0) + 1);
        }
    }
    let best = 0;
    for (const freq of counts.values()) best = Math.max(best, freq);
    return best;
};
