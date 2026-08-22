// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

#include <stdlib.h>
#include <string.h>

#define HS 200003
static long long hk[HS];
static char hu[HS];

static int hput(long long key) {
    unsigned i = (unsigned)(key % HS);
    if (key < 0) i = (unsigned)((-key) % HS);
    for (;;) {
        if (!hu[i]) { hu[i] = 1; hk[i] = key; return 1; }
        if (hk[i] == key) return 0;
        if (++i == HS) i = 0;
    }
}

int distinctPoints(char* s, int k) {
    int n = (int)strlen(s);
    int* f = (int*)calloc((size_t)(n + 1), sizeof(int));
    int* g = (int*)calloc((size_t)(n + 1), sizeof(int));
    int x = 0, y = 0;
    for (int i = 1; i <= n; i++) {
        char c = s[i - 1];
        if (c == 'U') y++;
        else if (c == 'D') y--;
        else if (c == 'L') x--;
        else x++;
        f[i] = x; g[i] = y;
    }
    memset(hu, 0, sizeof(hu));
    int ans = 0;
    for (int i = k; i <= n; i++) {
        int a = f[n] - (f[i] - f[i - k]);
        int b = g[n] - (g[i] - g[i - k]);
        long long key = (long long)a * n + b;
        ans += hput(key);
    }
    free(f); free(g);
    return ans;
}
