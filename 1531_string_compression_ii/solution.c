// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int memo1531[101][101];
static char* s1531;
static int n1531;

static int dp1531(int index, int remaining) {
    if (remaining < 0) return 1000000000;
    if (index == n1531 || n1531 - index <= remaining) return 0;
    if (memo1531[index][remaining] != -1) return memo1531[index][remaining];
    int answer = dp1531(index + 1, remaining - 1);
    int same = 0, removed = 0;
    for (int j = index; j < n1531; j++) {
        if (s1531[j] == s1531[index]) {
            same++;
            int encoded = 1 + (same >= 2) + (same >= 10) + (same >= 100);
            int cand = encoded + dp1531(j + 1, remaining - removed);
            if (cand < answer) answer = cand;
        } else {
            removed++;
            if (removed > remaining) break;
        }
    }
    return memo1531[index][remaining] = answer;
}

int getLengthOfOptimalCompression(char* s, int k) {
    s1531 = s;
    n1531 = (int)strlen(s);
    for (int i = 0; i <= n1531; i++)
        for (int j = 0; j <= k; j++) memo1531[i][j] = -1;
    return dp1531(0, k);
}
