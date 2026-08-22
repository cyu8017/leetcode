// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static const int MOD2801 = 1000000007;
static int memo2801[110][2][12][2];
static char* S2801;
static int N2801;

static int abs2801(int x) { return x < 0 ? -x : x; }

static int dfs2801(int pos, int tight, int last, int started) {
    if (pos == N2801) return started ? 1 : 0;
    if (memo2801[pos][tight][last + 1][started] != -1)
        return memo2801[pos][tight][last + 1][started];
    int up = tight ? (S2801[pos] - '0') : 9;
    int ans = 0;
    for (int d = 0; d <= up; d++) {
        int nt = tight && (d == up);
        if (!started) {
            if (d == 0) ans = (ans + dfs2801(pos + 1, nt, -1, 0)) % MOD2801;
            else ans = (ans + dfs2801(pos + 1, nt, d, 1)) % MOD2801;
        } else if (abs2801(d - last) == 1) {
            ans = (ans + dfs2801(pos + 1, nt, d, 1)) % MOD2801;
        }
    }
    return memo2801[pos][tight][last + 1][started] = ans;
}

static int countTo2801(char* s) {
    S2801 = s;
    N2801 = (int)strlen(s);
    memset(memo2801, -1, sizeof(memo2801));
    return dfs2801(0, 1, -1, 0);
}

static char* dec2801(const char* s) {
    int n = (int)strlen(s);
    char* b = (char*)malloc(n + 1);
    strcpy(b, s);
    int i = n - 1;
    while (i >= 0 && b[i] == '0') { b[i] = '9'; i--; }
    if (i >= 0) b[i]--;
    i = 0;
    while (i < n - 1 && b[i] == '0') i++;
    char* r = (char*)malloc(n - i + 1);
    strcpy(r, b + i);
    free(b);
    return r;
}

int countSteppingNumbers(char* low, char* high) {
    char* dlow = dec2801(low);
    int ans = countTo2801(high) - countTo2801(dlow);
    ans %= MOD2801;
    if (ans < 0) ans += MOD2801;
    free(dlow);
    return ans;
}
