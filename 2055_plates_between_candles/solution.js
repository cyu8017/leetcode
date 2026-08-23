// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[]}
 */
var platesBetweenCandles = function(s, queries) {
    const n = s.length;
    const pref = new Array(n + 1).fill(0);
    const left = new Array(n), right = new Array(n);
    let last = -1;
    for (let i = 0; i < n; i++) {
        pref[i + 1] = pref[i] + (s[i] === '*' ? 1 : 0);
        if (s[i] === '|') last = i;
        left[i] = last;
    }
    last = -1;
    for (let i = n - 1; i >= 0; i--) {
        if (s[i] === '|') last = i;
        right[i] = last;
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const l = right[queries[i][0]], r = left[queries[i][1]];
        if (l !== -1 && r !== -1 && l < r) ans[i] = pref[r] - pref[l];
        else ans[i] = 0;
    }
    return ans;
};
