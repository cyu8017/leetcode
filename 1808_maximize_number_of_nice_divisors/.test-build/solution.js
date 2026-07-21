"use strict";
// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/
function maxNiceDivisors(primeFactors) {
    const MOD = 1e9 + 7;
    const modPow = (base, exp) => {
        let result = 1n;
        let b = BigInt(base);
        let e = BigInt(exp);
        const m = BigInt(MOD);
        while (e > 0n) {
            if (e & 1n)
                result = (result * b) % m;
            b = (b * b) % m;
            e >>= 1n;
        }
        return Number(result);
    };
    if (primeFactors <= 3)
        return primeFactors;
    if (primeFactors % 3 === 0)
        return modPow(3, primeFactors / 3);
    if (primeFactors % 3 === 1)
        return (modPow(3, Math.floor(primeFactors / 3) - 1) * 4) % MOD;
    return (modPow(3, Math.floor(primeFactors / 3)) * 2) % MOD;
}
