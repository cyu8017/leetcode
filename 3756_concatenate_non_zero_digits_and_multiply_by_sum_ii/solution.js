// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum Ii
// https://leetcode.com/problems/concatenate_non_zero_digits_and_multiply_by_sum_ii/

var sumAndMultiply = function(s, queries) {
    const MX = 100001;
    const MOD = 1000000007n;
    const PW = new Array(MX);
    PW[0] = 1n;
    for (let i = 1; i < MX; i++) PW[i] = PW[i - 1] * 10n % MOD;
    const n = s.length;
    const sumD = new Array(n + 1).fill(0);
    const cntN0 = new Array(n + 1).fill(0);
    const p = new Array(n + 1).fill(0n);
    for (let i = 1; i <= n; i++) {
        const d = BigInt(s.charCodeAt(i - 1) - 48);
        sumD[i] = sumD[i - 1] + Number(d);
        cntN0[i] = cntN0[i - 1];
        if (d > 0n) {
            cntN0[i]++;
            p[i] = (p[i - 1] * 10n + d) % MOD;
        } else p[i] = p[i - 1];
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const l = queries[i][0], r = queries[i][1];
        const n0 = cntN0[r + 1] - cntN0[l];
        const sd = BigInt(sumD[r + 1] - sumD[l]);
        const x = (p[r + 1] - p[l] * PW[n0] % MOD + MOD) % MOD;
        ans[i] = Number(x * sd % MOD);
    }
    return ans;
};
