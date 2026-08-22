// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

#include <stdlib.h>

static int modPow(long long a, int b, int mod) {
    long long res = 1;
    a %= mod;
    while (b > 0) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return (int)res;
}

int numberOfSequence(int n, int* sick, int sickSize) {
    const int mod = 1000000007;
    int* fact = (int*)malloc((n + 1) * sizeof(int));
    int* invFact = (int*)malloc((n + 1) * sizeof(int));
    fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = (int)(1LL * fact[i - 1] * i % mod);
    invFact[n] = modPow(fact[n], mod - 2, mod);
    for (int i = n; i > 0; i--) invFact[i - 1] = (int)(1LL * invFact[i] * i % mod);
    int m = sickSize;
    int totalEmpty = n - m;
    long long ans = fact[totalEmpty];
    int prev = -1;
    for (int i = 0; i < m; i++) {
        int s = sick[i];
        int gap = s - prev - 1;
        if (prev == -1) ans = ans * invFact[gap] % mod;
        else if (gap > 0) ans = ans * invFact[gap] % mod * modPow(2, gap - 1, mod) % mod;
        prev = s;
    }
    int gap = n - prev - 1;
    ans = ans * invFact[gap] % mod;
    free(fact); free(invFact);
    return (int)ans;
}
