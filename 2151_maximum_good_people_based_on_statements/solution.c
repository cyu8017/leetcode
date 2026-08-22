// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

static int popcount2151(int x) {
    int c = 0;
    while (x) { c += x & 1; x >>= 1; }
    return c;
}

int maximumGood(int** statements, int statementsSize, int* statementsColSize) {
    (void)statementsColSize;
    int n = statementsSize, ans = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int ok = 1;
        for (int i = 0; i < n && ok; i++) {
            if ((mask & (1 << i)) == 0) continue;
            for (int j = 0; j < n; j++) {
                int s = statements[i][j];
                if (s == 2) continue;
                int goodJ = (mask & (1 << j)) != 0;
                if ((s == 1 && !goodJ) || (s == 0 && goodJ)) { ok = 0; break; }
            }
        }
        if (ok) {
            int c = popcount2151(mask);
            if (c > ans) ans = c;
        }
    }
    return ans;
}
