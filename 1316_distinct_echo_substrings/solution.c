// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { long long a, b; int len; } HashKey;

static int hash_eq(HashKey x, HashKey y) { return x.a == y.a && x.b == y.b && x.len == y.len; }

int distinctEchoSubstrings(char* text) {
    int n = (int)strlen(text);
    const long long mod1 = 1000000007LL, mod2 = 1000000009LL, base = 911382323LL;
    long long* h1 = (long long*)calloc(n + 1, sizeof(long long));
    long long* h2 = (long long*)calloc(n + 1, sizeof(long long));
    long long* p1 = (long long*)malloc((n + 1) * sizeof(long long));
    long long* p2 = (long long*)malloc((n + 1) * sizeof(long long));
    p1[0] = p2[0] = 1;
    for (int i = 0; i < n; i++) {
        int code = (unsigned char)text[i];
        h1[i + 1] = (h1[i] * base + code) % mod1;
        h2[i + 1] = (h2[i] * base + code) % mod2;
        p1[i + 1] = p1[i] * base % mod1;
        p2[i + 1] = p2[i] * base % mod2;
    }
    HashKey* echoes = (HashKey*)malloc(n * n * sizeof(HashKey));
    int en = 0;
    for (int half = 1; half <= n / 2; half++) {
        for (int left = 0; left <= n - 2 * half; left++) {
            int mid = left + half, right = left + 2 * half;
            long long a1 = (h1[mid] - h1[left] * p1[half] % mod1 + mod1) % mod1;
            long long b1 = (h2[mid] - h2[left] * p2[half] % mod2 + mod2) % mod2;
            long long a2 = (h1[right] - h1[mid] * p1[half] % mod1 + mod1) % mod1;
            long long b2 = (h2[right] - h2[mid] * p2[half] % mod2 + mod2) % mod2;
            if (a1 == a2 && b1 == b2) {
                HashKey key = {a1, b1, 2 * half};
                // full string hash
                long long fa = (h1[right] - h1[left] * p1[2 * half] % mod1 + mod1) % mod1;
                long long fb = (h2[right] - h2[left] * p2[2 * half] % mod2 + mod2) % mod2;
                key.a = fa; key.b = fb;
                bool found = false;
                for (int i = 0; i < en; i++) if (hash_eq(echoes[i], key)) { found = true; break; }
                if (!found) echoes[en++] = key;
            }
        }
    }
    free(h1); free(h2); free(p1); free(p2); free(echoes);
    return en;
}
