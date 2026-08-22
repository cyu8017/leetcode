// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

#include <stdlib.h>
#include <string.h>

int countPalindromes(char* s) {
    const int mod = 1000000007;
    int n = (int)strlen(s);
    int (*pref)[10][10] = calloc((size_t)n, sizeof(*pref));
    int cnt[10] = {0};
    for (int i = 0; i < n; i++) {
        if (i > 0) memcpy(pref[i], pref[i - 1], sizeof(pref[i]));
        int d = s[i] - '0';
        for (int a = 0; a < 10; a++) pref[i][a][d] += cnt[a];
        cnt[d]++;
    }
    int (*suf)[10][10] = calloc((size_t)n, sizeof(*suf));
    memset(cnt, 0, sizeof(cnt));
    for (int i = n - 1; i >= 0; i--) {
        if (i + 1 < n) memcpy(suf[i], suf[i + 1], sizeof(suf[i]));
        int d = s[i] - '0';
        for (int a = 0; a < 10; a++) suf[i][a][d] += cnt[a];
        cnt[d]++;
    }
    int ans = 0;
    for (int i = 2; i < n - 2; i++) {
        for (int a = 0; a < 10; a++)
            for (int b = 0; b < 10; b++)
                ans = (int)(((long long)ans + (long long)pref[i - 1][a][b] * suf[i + 1][a][b]) % mod);
    }
    free(pref); free(suf);
    return ans;
}
