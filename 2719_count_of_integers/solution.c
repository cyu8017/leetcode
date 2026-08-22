// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int minSum2719, maxSum2719;
static char* s2719;
static int n2719;
static int memo2719[23][401][2];
static bool vis2719[23][401][2];

static int dfs2719(int pos, int sum, int tight) {
    if (sum > maxSum2719) return 0;
    if (pos == n2719) return sum >= minSum2719 ? 1 : 0;
    if (vis2719[pos][sum][tight]) return memo2719[pos][sum][tight];
    vis2719[pos][sum][tight] = true;
    int up = tight ? s2719[pos] - '0' : 9;
    int res = 0;
    for (int d = 0; d <= up; d++)
        res = (res + dfs2719(pos + 1, sum + d, tight && d == up)) % 1000000007;
    return memo2719[pos][sum][tight] = res;
}

static int dp2719(char* s) {
    s2719 = s;
    n2719 = (int)strlen(s);
    memset(vis2719, 0, sizeof(vis2719));
    return dfs2719(0, 0, 1);
}

static char* dec2719(const char* s) {
    int len = (int)strlen(s);
    char* b = (char*)malloc((size_t)len + 1);
    strcpy(b, s);
    int i = len - 1;
    while (i >= 0 && b[i] == '0') { b[i] = '9'; i--; }
    if (i >= 0) b[i]--;
    int j = 0;
    while (j < len - 1 && b[j] == '0') j++;
    char* out = (char*)malloc((size_t)(len - j) + 1);
    strcpy(out, b + j);
    free(b);
    return out;
}

int count(char* num1, char* num2, int min_sum, int max_sum) {
    const int MOD = 1000000007;
    minSum2719 = min_sum;
    maxSum2719 = max_sum;
    char* d = dec2719(num1);
    int ans = (dp2719(num2) - dp2719(d) + MOD) % MOD;
    free(d);
    return ans;
}
