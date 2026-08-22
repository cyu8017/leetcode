// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

#include <stdlib.h>
#include <string.h>

int minOperations(char* s1, char* s2, int x) {
    int n = (int)strlen(s1);
    int* diff = (int*)malloc(n * sizeof(int));
    int m = 0;
    for (int i = 0; i < n; i++) if (s1[i] != s2[i]) diff[m++] = i;
    if (m % 2 == 1) { free(diff); return -1; }
    if (m == 0) { free(diff); return 0; }
    int* dp2 = (int*)malloc((m + 1) * sizeof(int));
    for (int i = 0; i <= m; i++) dp2[i] = 1 << 30;
    dp2[0] = 0;
    for (int i = 0; i < m; i++) {
        if (dp2[i] >= (1 << 30)) continue;
        if (i + 1 < m) {
            int cand = diff[i + 1] - diff[i];
            if (cand > x) cand = x;
            if (dp2[i] + cand < dp2[i + 2]) dp2[i + 2] = dp2[i] + cand;
        }
    }
    int ans = dp2[m] >= (1 << 30) ? -1 : dp2[m];
    free(diff); free(dp2);
    return ans;
}
