// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

var zigZagArrays = function(n, l, r) {
    const MOD = 1000000007;
    const m = r - l + 1;
    if (n === 1) return m % MOD;
    let up = new Array(m).fill(1);
    let down = new Array(m).fill(1);
    for (let length = 2; length <= n; length++) {
        const pref = new Array(m + 1).fill(0);
        for (let j = 0; j < m; j++) pref[j + 1] = (pref[j] + down[j]) % MOD;
        const nup = new Array(m);
        for (let j = 0; j < m; j++) nup[j] = pref[j];
        const suf = new Array(m + 1).fill(0);
        for (let j = m - 1; j >= 0; j--) suf[j] = (suf[j + 1] + up[j]) % MOD;
        const ndown = new Array(m);
        for (let j = 0; j < m; j++) ndown[j] = suf[j + 1];
        up = nup;
        down = ndown;
    }
    let ans = 0;
    for (let j = 0; j < m; j++) {
        ans = (ans + up[j]) % MOD;
        ans = (ans + down[j]) % MOD;
    }
    return ans;
};
