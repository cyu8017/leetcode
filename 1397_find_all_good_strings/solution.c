// LeetCode 1397 - Find All Good Strings
// https://leetcode.com/problems/find-all-good-strings/

#include <string.h>
#include <stdlib.h>

static int memo[501][51][2][2];
static int vis[501][51][2][2];
static int N, M, MOD;
static char *S1, *S2;
static int trans[51][26];

static int dp(int i, int j, int lo, int hi) {
    if (j == M) return 0;
    if (i == N) return 1;
    if (vis[i][j][lo][hi]) return memo[i][j][lo][hi];
    vis[i][j][lo][hi] = 1;
    int a = lo ? S1[i] - 'a' : 0;
    int b = hi ? S2[i] - 'a' : 25;
    long long ans = 0;
    for (int x = a; x <= b; x++)
        ans += dp(i + 1, trans[j][x], lo && x == a, hi && x == b);
    return memo[i][j][lo][hi] = (int)(ans % MOD);
}

int findGoodStrings(int n, char* s1, char* s2, char* evil) {
    MOD = 1000000007; N = n; M = (int)strlen(evil); S1 = s1; S2 = s2;
    memset(vis, 0, sizeof(vis));
    int* pi = (int*)calloc(M, sizeof(int));
    for (int i = 1; i < M; i++) {
        int j = pi[i - 1];
        while (j && evil[i] != evil[j]) j = pi[j - 1];
        if (evil[i] == evil[j]) j++;
        pi[i] = j;
    }
    for (int j = 0; j < M; j++) {
        for (int x = 0; x < 26; x++) {
            char c = 'a' + x;
            int k = j;
            while (k && evil[k] != c) k = pi[k - 1];
            if (evil[k] == c) k++;
            trans[j][x] = k;
        }
    }
    free(pi);
    return dp(0, 0, 1, 1);
}
