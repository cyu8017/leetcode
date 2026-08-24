// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

function check(s: any): any {
    if (s < 100) return s % 11 !== 0;
    const mid = Math.floor(s / 10) % 10;
    const last = s % 10;
    return mid > 1 && mid < last;
}export function countFancy(l: any, r: any): any {
    let num, n, f;
    const dfs = (pos, s, prev, st, lim) => {
        if (pos >= n) {
            if (st !== 3) return 1;
            return check(s) ? 1 : 0;
        }
        if (!lim && f[pos][s][prev][st] !== -1) return f[pos][s][prev][st];
        const up = lim ? num.charCodeAt(pos) - 48 : 9;
        let res = 0;
        for (let i = 0; i <= up; i++) {
            let nxtSt = st;
            if (st === 0) {
                if (prev === 0) nxtSt = 0;
                else if (i > prev) nxtSt = 1;
                else if (i < prev) nxtSt = 2;
                else nxtSt = 3;
            } else if (st === 1) {
                nxtSt = i > prev ? 1 : 3;
            } else if (st === 2) {
                nxtSt = i < prev ? 2 : 3;
            } else {
                nxtSt = 3;
            }
            res += dfs(pos + 1, s + i, i, nxtSt, lim && i === up);
        }
        if (!lim) f[pos][s][prev][st] = res;
        return res;
    };
    const calc = (x) => {
        if (x < 0) return 0;
        num = String(x);
        n = num.length;
        f = Array.from({length: n}, () =>
            Array.from({length: 9 * n + 1}, () =>
                Array.from({length: 10}, () => new Array(4).fill(-1))));
        return dfs(0, 0, 0, 0, true);
    };
    return calc(r) - calc(l - 1);
}
