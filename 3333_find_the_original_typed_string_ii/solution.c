// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

#include <stdlib.h>
#include <string.h>

int possibleStringCount(char* word, int k) {
    const int mod = 1000000007;
    int n = (int)strlen(word);
    int* groups = (int*)malloc((size_t)n * sizeof(int));
    int gn = 0;
    for (int i = 0; i < n; ) {
        int j = i;
        while (j < n && word[j] == word[i]) j++;
        groups[gn++] = j - i;
        i = j;
    }
    int total = 1;
    for (int i = 0; i < gn; i++) total = (int)((long long)total * groups[i] % mod);
    if (k <= gn) { free(groups); return total; }
    int need = k - 1;
    int* dp = (int*)calloc((size_t)need, sizeof(int));
    dp[0] = 1;
    for (int gi = 0; gi < gn; gi++) {
        int g = groups[gi];
        int* ndp = (int*)calloc((size_t)need, sizeof(int));
        int* pref = (int*)calloc((size_t)(need + 1), sizeof(int));
        for (int i = 0; i < need; i++) pref[i + 1] = (pref[i] + dp[i]) % mod;
        for (int s = 0; s < need; s++) {
            int lo = s - g; if (lo < 0) lo = 0;
            int hi = s - 1;
            if (hi >= 0) ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod;
        }
        free(dp); free(pref); dp = ndp;
    }
    int bad = 0;
    for (int i = 0; i < need; i++) bad = (bad + dp[i]) % mod;
    free(dp); free(groups);
    return (total - bad + mod) % mod;
}
