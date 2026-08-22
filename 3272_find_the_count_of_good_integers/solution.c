// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct { char* key; int used; } Seen;

static int cmpChar(const void* a, const void* b) {
    return (*(const char*)a > *(const char*)b) - (*(const char*)a < *(const char*)b);
}

long long countGoodIntegers(int n, int k) {
    int half = (n + 1) / 2;
    int start = 1;
    for (int i = 1; i < half; i++) start *= 10;
    int end = start * 10;
    long long* fact = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i;
    int scap = 10007;
    Seen* seen = (Seen*)calloc((size_t)scap, sizeof(Seen));
    long long ans = 0;
    for (int h = start; h < end; h++) {
        char s[32], pal[64];
        sprintf(s, "%d", h);
        int sl = (int)strlen(s);
        strcpy(pal, s);
        int revStart = sl - 1;
        if (n % 2 == 1) revStart--;
        int pl = sl;
        for (int i = revStart; i >= 0; i--) pal[pl++] = s[i];
        pal[pl] = 0;
        long long val = 0;
        for (int i = 0; pal[i]; i++) val = val * 10 + (pal[i] - '0');
        if (val % k != 0) continue;
        char key[64]; strcpy(key, pal);
        qsort(key, (size_t)pl, 1, cmpChar);
        unsigned hh = 2166136261u;
        for (int i = 0; key[i]; i++) { hh ^= (unsigned)key[i]; hh *= 16777619u; }
        int idx = (int)(hh % (unsigned)scap);
        int found = 0;
        for (int t = 0; t < scap; t++) {
            int i = (idx + t) % scap;
            if (!seen[i].used) {
                seen[i].used = 1;
                seen[i].key = strdup(key);
                break;
            }
            if (strcmp(seen[i].key, key) == 0) { found = 1; break; }
        }
        if (found) continue;
        int cnt[10] = {0};
        for (int i = 0; key[i]; i++) cnt[key[i] - '0']++;
        long long total = fact[n];
        for (int c = 0; c < 10; c++) total /= fact[cnt[c]];
        if (cnt[0] > 0) {
            long long bad = fact[n - 1];
            cnt[0]--;
            for (int c = 0; c < 10; c++) bad /= fact[cnt[c]];
            cnt[0]++;
            total -= bad;
        }
        ans += total;
    }
    for (int i = 0; i < scap; i++) if (seen[i].used) free(seen[i].key);
    free(seen); free(fact);
    return ans;
}
