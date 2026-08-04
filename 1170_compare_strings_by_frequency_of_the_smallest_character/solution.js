// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

/**
 * @param {string[]} queries
 * @param {string[]} words
 * @return {number[]}
 */
var numSmallerByFrequency = function(queries, words) {
    const f = (s) => {
        let min = "z", cnt = 0;
        for (const ch of s) {
            if (ch < min) { min = ch; cnt = 1; }
            else if (ch === min) cnt++;
        }
        return cnt;
    };
    const freqs = words.map(f).sort((a, b) => a - b);
    const bisectRight = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    return queries.map((q) => freqs.length - bisectRight(freqs, f(q)));
};
