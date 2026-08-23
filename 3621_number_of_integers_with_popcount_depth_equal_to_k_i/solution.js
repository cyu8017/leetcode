// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

var popcountDepth = function(n, k) {
    if (k === 0) return n >= 1 ? 1 : 0;
    const bitCount = (x) => {
        let c = 0;
        while (x) { c += x & 1; x >>>= 1; }
        return c;
    };
    const depth = (x) => {
        if (x <= 0) return 100;
        let d = 0;
        while (x > 1) {
            x = bitCount(x);
            d++;
        }
        return d;
    };
    let s = '';
    for (let x = n; x > 0; x = Math.floor(x / 2)) s += String(x & 1);
    s = s.split('').reverse().join('');
    if (s.length === 0) s = '0';
    const memo = new Map();
    const dfs = (pos, tight, started, pc) => {
        if (pos === s.length) {
            if (started === 0) return 0;
            if (pc === 1) return k === 1 ? 1 : 0;
            return depth(pc) === k - 1 ? 1 : 0;
        }
        const key = pos + ',' + tight + ',' + started + ',' + pc;
        if (memo.has(key)) return memo.get(key);
        const up = tight === 1 ? Number(s[pos]) : 1;
        let res = 0;
        for (let dig = 0; dig <= up; dig++) {
            const nt = (tight === 1 && dig === up) ? 1 : 0;
            if (started === 0 && dig === 0) res += dfs(pos + 1, nt, 0, 0);
            else res += dfs(pos + 1, nt, 1, pc + dig);
        }
        memo.set(key, res);
        return res;
    };
    return dfs(0, 1, 0, 0);
};
