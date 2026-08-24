// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

function dfs(res: any, i: any, tight: any, sameLen: any, num: any, t: any): any {
    if (i === res.length) {
        let prod = 1;
        for (const c of res) {
            prod *= (c.charCodeAt(0) - 48);
            if (prod === 0) break;
        }
        return prod % t === 0 && prod > 0;
    }
    let start = (i === 0) ? '1' : '0';
    if (tight && sameLen && i < num.length) start = num[i];
    for (let cc = start.charCodeAt(0); cc <= 57; cc++) {
        const c = String.fromCharCode(cc);
        res[i] = c;
        const nt = tight && sameLen && i < num.length && c === num[i];
        if (dfs(res, i + 1, nt, sameLen, num, t)) return true;
    }
    return false;
}export function smallestNumber(num: any, t: any): any {
    let tt = t;
    for (let d = 9; d >= 2; d--) {
        while (tt % d === 0) tt = Math.floor(tt / d);
    }
    if (tt > 1) return '-1';
    for (let extra = 0; extra <= 60; extra++) {
        const L = num.length + extra;
        const res = new Array(L);
        if (dfs(res, 0, true, extra === 0, num, t)) return res.join('');
    }
    return '-1';
}
