// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

export function numberOfWays(startPos: number, endPos: number, k: number): number {
    const mod = 1000000007;
    const modPow = (a, e) => {
        let res = 1n, base = BigInt(a) % BigInt(mod);
        let ee = BigInt(e);
        while (ee > 0n) {
            if (ee & 1n) res = res * base % BigInt(mod);
            base = base * base % BigInt(mod);
            ee >>= 1n;
        }
        return Number(res);
    };
    const comb = (n, r) => {
        if (r < 0 || r > n) return 0;
        let num = 1n, den = 1n;
        for (let i = 0; i < r; i++) {
            num = num * BigInt(n - i) % BigInt(mod);
            den = den * BigInt(i + 1) % BigInt(mod);
        }
        return Number(num * BigInt(modPow(Number(den), mod - 2)) % BigInt(mod));
    };
    const diff = Math.abs(endPos - startPos);
    if (diff > k || (k - diff) % 2 !== 0) return 0;
    const r = (k + diff) / 2;
    return comb(k, r);
}
