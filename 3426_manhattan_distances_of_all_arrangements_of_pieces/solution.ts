// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

export function distanceSum(m: any, n: any, k: any): any {
    const mod = 1000000007;
    const modPow = (a, e) => {
        let r = 1n;
        let base = BigInt(a % mod);
        let exp = BigInt(e);
        const MOD = BigInt(mod);
        while (exp > 0n) {
            if (exp & 1n) r = (r * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return Number(r);
    };
    const comb = (nn, kk) => {
        if (kk < 0 || kk > nn) return 0;
        let num = 1, den = 1;
        for (let i = 0; i < kk; i++) {
            num = Number(BigInt(num) * BigInt(nn - i) % BigInt(mod));
            den = Number(BigInt(den) * BigInt(i + 1) % BigInt(mod));
        }
        return Number(BigInt(num) * BigInt(modPow(den, mod - 2)) % BigInt(mod));
    };
    if (k < 2) return 0;
    const totalCells = m * n;
    const pairChoose = comb(totalCells - 2, k - 2);
    let sumDist = 0n;
    for (let d = 1; d < m; d++) sumDist += BigInt(d) * BigInt(m - d) * BigInt(n) * BigInt(n);
    for (let d = 1; d < n; d++) sumDist += BigInt(d) * BigInt(n - d) * BigInt(m) * BigInt(m);
    return Number(sumDist % BigInt(mod) * BigInt(pairChoose) % BigInt(mod));
}
