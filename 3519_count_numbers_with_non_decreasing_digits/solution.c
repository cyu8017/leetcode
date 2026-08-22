// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

#include <stdlib.h>
#include <string.h>

#define MOD3519 1000000007

/* Convert decimal string to base-b digits (MSB first) via repeated division */
static int* toDigits(const char* s, int b, int* outLen) {
    int n = (int)strlen(s);
    int* num = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) num[i] = s[i] - '0';
    int* digs = (int*)malloc((size_t)(n * 8 + 8) * sizeof(int));
    int dc = 0;
    int allZero = 1;
    for (int i = 0; i < n; i++) if (num[i]) allZero = 0;
    if (allZero) {
        digs[0] = 0; *outLen = 1; free(num); return digs;
    }
    while (1) {
        allZero = 1;
        for (int i = 0; i < n; i++) if (num[i]) { allZero = 0; break; }
        if (allZero) break;
        long long rem = 0;
        for (int i = 0; i < n; i++) {
            rem = rem * 10 + num[i];
            num[i] = (int)(rem / b);
            rem %= b;
        }
        digs[dc++] = (int)rem;
    }
    for (int i = 0, j = dc - 1; i < j; i++, j--) {
        int t = digs[i]; digs[i] = digs[j]; digs[j] = t;
    }
    *outLen = dc;
    free(num);
    return digs;
}

static char* decStr(const char* s) {
    int n = (int)strlen(s);
    char* out = (char*)malloc((size_t)n + 1);
    memcpy(out, s, (size_t)n + 1);
    int i = n - 1;
    while (i >= 0 && out[i] == '0') { out[i] = '9'; i--; }
    if (i < 0) { free(out); char* z = (char*)malloc(2); z[0] = '0'; z[1] = '\0'; return z; }
    out[i]--;
    /* strip leading zeros except keep one */
    int st = 0;
    while (st + 1 < n && out[st] == '0') st++;
    if (st) memmove(out, out + st, (size_t)(n - st + 1));
    return out;
}

static int b3519;
static int* digs3519;
static int m3519;
static int memo3519[400][11][2];
static char seen3519[400][11][2];

static int dfs3519(int pos, int last, int tight) {
    if (pos == m3519) return 1;
    if (seen3519[pos][last][tight]) return memo3519[pos][last][tight];
    int up = tight ? digs3519[pos] : (b3519 - 1);
    int res = 0;
    for (int d = last; d <= up; d++) {
        res = (res + dfs3519(pos + 1, d, tight && d == up)) % MOD3519;
    }
    seen3519[pos][last][tight] = 1;
    memo3519[pos][last][tight] = res;
    return res;
}

static int countUpto(const char* s) {
    digs3519 = toDigits(s, b3519, &m3519);
    memset(seen3519, 0, sizeof(seen3519));
    int ans = dfs3519(0, 0, 1);
    free(digs3519);
    return ans;
}

int countNumbers(char* l, char* r, int b) {
    b3519 = b;
    char* ld = decStr(l);
    int ans = (countUpto(r) - countUpto(ld) + MOD3519) % MOD3519;
    free(ld);
    return ans;
}
