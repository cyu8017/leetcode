// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

/**
 * @param {string} s1
 * @param {string} s2
 * @return {string}
 */
var minWindow = function(s1, s2) {
    const m = s1.length, n = s2.length;
    let best = '';
    let i = 0;
    while (i < m) {
        let j = 0, k = i;
        while (k < m && j < n) {
            if (s1[k] === s2[j]) j++;
            k++;
        }
        if (j < n) break;
        const end = k - 1;
        j = n - 1;
        k = end;
        while (j >= 0) {
            if (s1[k] === s2[j]) j--;
            k--;
        }
        const start = k + 1;
        if (best.length === 0 || end - start + 1 < best.length) best = s1.substring(start, end + 1);
        i = start + 1;
    }
    return best;
};
