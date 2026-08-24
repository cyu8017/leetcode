// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

export function processStr(s: any, k: any): any {
    let m = 0n;
    const kk = BigInt(k);
    for (const c of s) {
        if (c === '*') m = m > 0n ? m - 1n : 0n;
        else if (c === '#') m <<= 1n;
        else if (c !== '%') m += 1n;
    }
    let k2 = kk;
    if (k2 >= m) return '.';
    for (let i = s.length - 1; ; i--) {
        const c = s[i];
        if (c === '*') m += 1n;
        else if (c === '#') {
            m /= 2n;
            if (k2 >= m) k2 -= m;
        } else if (c === '%') {
            k2 = m - 1n - k2;
        } else {
            m -= 1n;
            if (k2 === m) return c;
        }
    }
}
