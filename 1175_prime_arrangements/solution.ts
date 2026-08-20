// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

function numPrimeArrangements(n: number): number {
    const MOD = 1e9 + 7;
    const isPrime = (x) => {
        if (x < 2) return false;
        for (let d = 2; d * d <= x; d++) if (x % d === 0) return false;
        return true;
    };
    let primes = 0;
    for (let i = 1; i <= n; i++) if (isPrime(i)) primes++;
    const fact = (x) => {
        let r = 1;
        for (let i = 2; i <= x; i++) r = (r * i) % MOD;
        return r;
    };
    return (fact(primes) * fact(n - primes)) % MOD;
}
