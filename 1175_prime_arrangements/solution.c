// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

static int isPrime(int x) {
    if (x < 2) return 0;
    for (int d = 2; d * d <= x; d++) if (x % d == 0) return 0;
    return 1;
}

static long long factMod(int n, int MOD) {
    long long r = 1;
    for (int i = 2; i <= n; i++) r = r * i % MOD;
    return r;
}

int numPrimeArrangements(int n) {
    const int MOD = 1000000007;
    int primes = 0;
    for (int i = 1; i <= n; i++) if (isPrime(i)) primes++;
    return (int)(factMod(primes, MOD) * factMod(n - primes, MOD) % MOD);
}
