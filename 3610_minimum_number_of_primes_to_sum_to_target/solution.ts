// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

const primes3610 = [];
function ensurePrimes3610(): any {
    if (primes3610.length > 0) return;
    let x = 2;
    while (primes3610.length < 1000) {
        let isPrime = true;
        for (const p of primes3610) {
            if (p * p > x) break;
            if (x % p === 0) { isPrime = false; break; }
        }
        if (isPrime) primes3610.push(x);
        x++;
    }
}export function minNumberOfPrimes(n: any, m: any): any {
    ensurePrimes3610();
    const Inf = Math.floor(2147483647 / 2);
    const f = new Array(n + 1).fill(Inf);
    f[0] = 0;
    for (let pi = 0; pi < m; pi++) {
        const x = primes3610[pi];
        for (let i = x; i <= n; i++)
            if (f[i - x] + 1 < f[i]) f[i] = f[i - x] + 1;
    }
    return f[n] < Inf ? f[n] : -1;
}
