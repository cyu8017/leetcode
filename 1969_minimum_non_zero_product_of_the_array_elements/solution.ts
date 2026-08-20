// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

function minNonZeroProduct(p: number): number {
    const MOD = 1000000007n;
    const mx = (1n << BigInt(p)) - 1n;
    const modPow = (base: any, exp: any) => {
        let r = 1n, b = base % MOD, e = exp;
        while (e > 0n) {
            if (e & 1n) r = r * b % MOD;
            b = b * b % MOD;
            e >>= 1n;
        }
        return r;
    };
    return Number(mx % MOD * modPow(mx - 1n, (1n << BigInt(p - 1)) - 1n) % MOD);
}
