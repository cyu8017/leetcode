// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

export function minimumCost(target: any, words: any, costs: any): any {
    const bas = 13331n, mod = 998244353n;
    const inf = Math.floor(Number.MAX_SAFE_INTEGER / 2);
    const n = target.length;
    const p = new Array(n + 1), h = new Array(n + 1);
    p[0] = 1n; h[0] = 0n;
    for (let i = 1; i <= n; i++) {
        p[i] = (p[i - 1] * bas) % mod;
        h[i] = (h[i - 1] * bas + BigInt(target.charCodeAt(i - 1))) % mod;
    }
    const query = (l, r) => Number((h[r] - (h[l - 1] * p[r - l + 1]) % mod + mod) % mod);
    const f = new Array(n + 1).fill(inf);
    f[0] = 0;
    const ss = new Set();
    for (const w of words) ss.add(w.length);
    const lengths = [...ss].sort((a, b) => a - b);
    const d = new Map();
    for (let i = 0; i < words.length; i++) {
        let x = 0n;
        for (let c = 0; c < words[i].length; c++) x = (x * bas + BigInt(words[i].charCodeAt(c))) % mod;
        const key = Number(x);
        if (!d.has(key) || costs[i] < d.get(key)) d.set(key, costs[i]);
    }
    for (let i = 1; i <= n; i++) {
        for (const j of lengths) {
            if (j > i) break;
            const x = query(i - j + 1, i);
            if (d.has(x)) f[i] = Math.min(f[i], f[i - j] + d.get(x));
        }
    }
    return f[n] >= inf ? -1 : f[n];
}
