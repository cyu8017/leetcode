// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

/**
 * @param {string} s
 * @return {number}
 */
var equalDigitFrequency = function(s) {
    const n = s.length;
    const seen = new Set();
    for (let i = 0; i < n; i++) {
        const freq = new Array(10).fill(0);
        let maxf = 0, kinds = 0;
        for (let j = i; j < n; j++) {
            const d = s.charCodeAt(j) - 48;
            if (freq[d] === 0) kinds++;
            freq[d]++;
            maxf = Math.max(maxf, freq[d]);
            if (maxf * kinds === j - i + 1) seen.add(s.substring(i, j + 1));
        }
    }
    return seen.size;
};
