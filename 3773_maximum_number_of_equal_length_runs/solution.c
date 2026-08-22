// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

#include <string.h>

int maxSameLengthRuns(char* s) {
    int n = (int)strlen(s);
    int cnt[100005];
    memset(cnt, 0, sizeof(cnt));
    int ans = 0;
    for (int i = 0; i < n; ) {
        int j = i + 1;
        while (j < n && s[j] == s[i]) j++;
        int m = j - i;
        if (m < 100005) {
            cnt[m]++;
            if (cnt[m] > ans) ans = cnt[m];
        }
        i = j;
    }
    return ans;
}
