// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

#include <stdlib.h>
#include <string.h>

static int modPow3343(long long a, long long e, int mod) {
    long long r = 1;
    while (e > 0) {
        if (e & 1) r = r * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return (int)r;
}

int countBalancedPermutations(char* num) {
    const int mod = 1000000007;
    int cnt[10] = {0};
    int sum = 0, n = (int)strlen(num);
    for (int i = 0; i < n; i++) {
        int d = num[i] - '0';
        cnt[d]++;
        sum += d;
    }
    if (sum % 2 == 1) return 0;
    int halfN = n / 2, halfS = sum / 2;
    int* fact = (int*)malloc((n + 1) * sizeof(int));
    int* invF = (int*)malloc((n + 1) * sizeof(int));
    fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = (int)((long long)fact[i - 1] * i % mod);
    invF[n] = modPow3343(fact[n], mod - 2, mod);
    for (int i = n; i > 0; i--) invF[i - 1] = (int)((long long)invF[i] * i % mod);

    /* map (used,s) -> ways using flat array of size (halfN+1)*(halfS+1) */
    int dim = (halfN + 1) * (halfS + 1);
    int* dp = (int*)calloc(dim, sizeof(int));
    int* ndp = (int*)calloc(dim, sizeof(int));
    dp[0] = 1;
    for (int d = 0; d <= 9; d++) {
        memset(ndp, 0, dim * sizeof(int));
        for (int used = 0; used <= halfN; used++) {
            for (int s = 0; s <= halfS; s++) {
                int ways = dp[used * (halfS + 1) + s];
                if (!ways) continue;
                for (int take = 0; take <= cnt[d]; take++) {
                    int nu = used + take, ns = s + take * d;
                    if (nu > halfN || ns > halfS) continue;
                    long long w = (long long)ways * invF[take] % mod * invF[cnt[d] - take] % mod;
                    ndp[nu * (halfS + 1) + ns] = (ndp[nu * (halfS + 1) + ns] + (int)w) % mod;
                }
            }
        }
        int* tmp = dp; dp = ndp; ndp = tmp;
    }
    long long ans = dp[halfN * (halfS + 1) + halfS];
    ans = ans * fact[halfN] % mod * fact[n - halfN] % mod;
    for (int d = 0; d <= 9; d++) ans = ans * fact[cnt[d]] % mod;
    free(fact); free(invF); free(dp); free(ndp);
    return (int)ans;
}
