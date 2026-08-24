// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

function modPow(a: any, e: any, mod: any): any {
    let r = 1;
    a %= mod;
    while (e > 0) {
        if (e & 1) r = r * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return r;
}function key(a: any, b: any): any {
    return (BigInt(a) << 32n) | BigInt(b >>> 0);
}export function countBalancedPermutations(num: any): any {
    const mod = 1000000007;
    const cnt = new Array(10).fill(0);
    let sum = 0;
    for (const c of num) {
        cnt[c.charCodeAt(0) - 48]++;
        sum += c.charCodeAt(0) - 48;
    }
    if (sum % 2 === 1) return 0;
    const n = num.length;
    const halfN = Math.floor(n / 2), halfS = Math.floor(sum / 2);
    const fact = new Array(n + 1), invF = new Array(n + 1);
    fact[0] = 1;
    for (let i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % mod;
    invF[n] = modPow(fact[n], mod - 2, mod);
    for (let i = n; i > 0; i--) invF[i - 1] = invF[i] * i % mod;
    let dp = new Map();
    dp.set(key(0, 0), 1);
    for (let d = 0; d <= 9; d++) {
        const ndp = new Map();
        for (const [st, ways] of dp) {
            const used = Number(st >> 32n);
            const s = Number(st & 0xffffffffn);
            for (let take = 0; take <= cnt[d]; take++) {
                const nu = used + take, ns = s + take * d;
                if (nu > halfN || ns > halfS) continue;
                const w = ways * invF[take] % mod * invF[cnt[d] - take] % mod;
                const nk = key(nu, ns);
                ndp.set(nk, ((ndp.get(nk) || 0) + w) % mod);
            }
        }
        dp = ndp;
    }
    let ans = dp.get(key(halfN, halfS)) || 0;
    ans = ans * fact[halfN] % mod * fact[n - halfN] % mod;
    for (let d = 0; d <= 9; d++) ans = ans * fact[cnt[d]] % mod;
    return ans;
}
