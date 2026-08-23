// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

const MOD = 1000000007;
function toDigits(s, b) {
    if (s === '0') return [0];
    const digs = [];
    while (!(s.length === 1 && s[0] === '0')) {
        let rem = 0;
        let q = '';
        for (const c of s) {
            const cur = rem * 10 + (c.charCodeAt(0) - 48);
            const d = Math.floor(cur / b);
            rem = cur % b;
            if (q.length > 0 || d !== 0) q += String(d);
        }
        digs.push(rem);
        s = q.length === 0 ? '0' : q;
    }
    digs.reverse();
    return digs;
}
function dec(s) {
    const a = s.split('');
    let i = a.length - 1;
    while (i >= 0 && a[i] === '0') { a[i] = '9'; i--; }
    if (i < 0) return '0';
    a[i] = String(a[i].charCodeAt(0) - 49);
    let t = a.join('');
    let p = 0;
    while (p + 1 < t.length && t[p] === '0') p++;
    return t.substring(p);
}
function countUpto(digs, b) {
    const m = digs.length;
    const memo = new Map();
    function dfs(pos, last, tight) {
        if (pos === m) return 1;
        const key = pos + ',' + last + ',' + (tight ? 1 : 0);
        if (memo.has(key)) return memo.get(key);
        const up = tight ? digs[pos] : b - 1;
        let res = 0;
        for (let d = last; d <= up; d++)
            res = (res + dfs(pos + 1, d, tight && d === up)) % MOD;
        memo.set(key, res);
        return res;
    }
    return dfs(0, 0, true);
}
var countNumbers = function(l, r, b) {
    const rd = toDigits(r, b);
    const ld = toDigits(dec(l), b);
    return (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD;
};
