// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

var zigZagArrays = function(n, l, r) {
    const MOD = 1000000007;
    const m = r - l + 1;
    if (n === 1) return m % MOD;
    let up = new Array(m).fill(1);
    let down = new Array(m).fill(1);
    for (let len_ = 2; len_ <= n; len_++) {
        const prefDown = new Array(m + 1).fill(0);
        for (let j = 0; j < m; j++) prefDown[j + 1] = (prefDown[j] + down[j]) % MOD;
        const nup = new Array(m);
        for (let j = 0; j < m; j++) nup[j] = prefDown[j];
        const sufUp = new Array(m + 1).fill(0);
        for (let j = m - 1; j >= 0; j--) sufUp[j] = (sufUp[j + 1] + up[j]) % MOD;
        const ndown = new Array(m);
        for (let j = 0; j < m; j++) ndown[j] = sufUp[j + 1];
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
