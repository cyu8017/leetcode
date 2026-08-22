// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

#include <stdio.h>
#include <string.h>

static char s3490[12];
static int len3490;

static int dfs3490(int pos, int tight, int sum, int prod, int started) {
    if (pos == len3490) {
        if (!started) return 0;
        if (sum > 0 && prod % sum == 0) return 1;
        return 0;
    }
    int up = tight ? (s3490[pos] - '0') : 9;
    int ans = 0;
    for (int d = 0; d <= up; d++) {
        int nt = tight && (d == up);
        if (!started && d == 0) {
            ans += dfs3490(pos + 1, nt, 0, 1, 0);
        } else {
            int ns = sum + d;
            int np = !started ? d : prod * d;
            ans += dfs3490(pos + 1, nt, ns, np, 1);
        }
    }
    return ans;
}

static int countBeautiful(int n) {
    if (n <= 0) return 0;
    sprintf(s3490, "%d", n);
    len3490 = (int)strlen(s3490);
    return dfs3490(0, 1, 0, 1, 0);
}

int beautifulNumbers(int l, int r) {
    return countBeautiful(r) - countBeautiful(l - 1);
}
