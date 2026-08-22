// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

#include <stdlib.h>
#include <string.h>

typedef struct {
    long long *p, *h, mod;
} Hashing;

static Hashing* newHashing(const char* word, long long base, long long mod) {
    int n = (int)strlen(word);
    Hashing* hs = (Hashing*)malloc(sizeof(Hashing));
    hs->p = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    hs->h = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    hs->mod = mod;
    hs->p[0] = 1; hs->h[0] = 0;
    for (int i = 1; i <= n; i++) {
        hs->p[i] = (hs->p[i - 1] * base) % mod;
        hs->h[i] = (hs->h[i - 1] * base + (word[i - 1] - 'a')) % mod;
    }
    return hs;
}
static long long queryH(Hashing* hs, int l, int r) {
    return (hs->h[r] - hs->h[l - 1] * hs->p[r - l + 1] % hs->mod + hs->mod) % hs->mod;
}

int minimumTimeToInitialState(char* word, int k) {
    Hashing* hashing = newHashing(word, 13331, 998244353);
    int n = (int)strlen(word);
    int ans = (n + k - 1) / k;
    for (int i = k; i < n; i += k) {
        if (queryH(hashing, 1, n - i) == queryH(hashing, i + 1, n)) {
            ans = i / k;
            break;
        }
    }
    free(hashing->p); free(hashing->h); free(hashing);
    return ans;
}
