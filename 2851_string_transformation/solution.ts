// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

export function numberOfWays(s: string, t: string, k: number): number {
    const MOD = 1000000007n;
    const n = s.length;
    const ss = s + s;
    if (!ss.slice(0, 2 * n - 1).includes(t)) return 0;
    let cnt = 0;
    for (let i = 0; i < n; i++) if (ss.slice(i, i + n) === t) cnt++;
    const same = s === t;
    const modPow = (a, b) => {
        let res = 1n;
        a %= MOD;
        let bb = BigInt(b);
        while (bb > 0n) {
            if (bb & 1n) res = (res * a) % MOD;
            a = (a * a) % MOD;
            bb >>= 1n;
        }
        return res;
    };
    const pk = modPow(BigInt(n - 1), k);
    const invn = modPow(BigInt(n), MOD - 2n);
    const sign = (BigInt(k) % 2n === 1n) ? MOD - 1n : 1n;
    const waysSame = Number(((pk + BigInt((n - 1) % Number(MOD)) * sign % MOD) % MOD * invn) % MOD);
    const waysDiff = Number(((pk - sign + MOD) % MOD * invn) % MOD);
    if (same) return waysSame;
    return Number((BigInt(waysDiff) * BigInt(cnt)) % MOD);
}
