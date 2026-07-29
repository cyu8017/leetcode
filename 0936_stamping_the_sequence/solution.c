// LeetCode 0936 - Stamping the Sequence
// https://leetcode.com/problems/stamping-the-sequence/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int* movesToStamp(char* stamp, char* target, int* returnSize) {
    int n = (int)strlen(target), m = (int)strlen(stamp);
    bool* done = (bool*)calloc((size_t)n, sizeof(bool));
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int an = 0;
    int changed = 1;
    while (changed) {
        changed = 0;
        for (int i = n - m; i >= 0; i--) {
            int ok = 1, any = 0;
            for (int j = 0; j < m; j++) {
                if (!done[i + j] && target[i + j] != stamp[j]) { ok = 0; break; }
                if (!done[i + j]) any = 1;
            }
            if (ok && any) {
                for (int j = 0; j < m; j++) done[i + j] = true;
                ans[an++] = i;
                changed = 1;
                break;
            }
        }
    }
    int all = 1;
    for (int i = 0; i < n; i++) if (!done[i]) { all = 0; break; }
    free(done);
    if (!all) { *returnSize = 0; free(ans); return NULL; }
    for (int i = 0; i < an / 2; i++) {
        int t = ans[i]; ans[i] = ans[an - 1 - i]; ans[an - 1 - i] = t;
    }
    *returnSize = an;
    return ans;
}
