// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

/**
 * @param {string} s
 * @return {number}
 */
var countPalindromes = function(s) {
    const mod = 1000000007;
    const n = s.length;
    const pref = Array.from({ length: n }, () => Array.from({ length: 10 }, () => Array(10).fill(0)));
    const suf = Array.from({ length: n }, () => Array.from({ length: 10 }, () => Array(10).fill(0)));
    const cnt = Array(10).fill(0);
    for (let i = 0; i < n; i++) {
        if (i > 0) {
            for (let a = 0; a < 10; a++)
                for (let b = 0; b < 10; b++) pref[i][a][b] = pref[i - 1][a][b];
        }
        const d = s.charCodeAt(i) - 48;
        for (let a = 0; a < 10; a++) pref[i][a][d] += cnt[a];
        cnt[d]++;
    }
    cnt.fill(0);
    for (let i = n - 1; i >= 0; i--) {
        if (i + 1 < n) {
            for (let a = 0; a < 10; a++)
                for (let b = 0; b < 10; b++) suf[i][a][b] = suf[i + 1][a][b];
        }
        const d = s.charCodeAt(i) - 48;
        for (let a = 0; a < 10; a++) suf[i][a][d] += cnt[a];
        cnt[d]++;
    }
    let ans = 0;
    for (let i = 2; i < n - 2; i++) {
        for (let a = 0; a < 10; a++) {
            for (let b = 0; b < 10; b++) {
                ans = (ans + pref[i - 1][a][b] * suf[i + 1][a][b]) % mod;
            }
        }
    }
    return ans;
};
