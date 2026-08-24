// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

function bitsPop(x) {
    let c = 0;
    while (x > 0) { c += x & 1; x >>= 1; }
    return c;
}
var countKReducibleNumbers = function(s, k) {
    const mod = 1000000007;
    const red = new Array(801);
    red[1] = 0;
    for (let i = 2; i <= 800; i++) red[i] = 1 + red[bitsPop(i)];
    const memo = new Map();
    const key = (pos, tight, ones) => (BigInt(pos) << 32n) | (BigInt(tight) << 16n) | BigInt(ones);
    const dfs = (pos, tight, ones) => {
        if (pos === s.length) {
            if (ones === 0) return 0;
            return red[ones] <= k - 1 ? 1 : 0;
        }
        const ky = key(pos, tight ? 1 : 0, ones);
        if (memo.has(ky)) return memo.get(ky);
        const up = tight ? (s.charCodeAt(pos) - 48) : 1;
        let ans = 0;
        for (let d = 0; d <= up; d++) {
            const nt = tight && d === up;
            ans = (ans + dfs(pos + 1, nt, ones + d)) % mod;
        }
        memo.set(ky, ans);
        return ans;
    };
    return dfs(0, true, 0);
};
