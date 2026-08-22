// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

#include <stdlib.h>
#include <string.h>

int countValidSelections(int* nums, int numsSize) {
    int n = numsSize, ans = 0;
    int* a = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        if (nums[i] != 0) continue;
        int dirs[2] = {-1, 1};
        for (int di = 0; di < 2; di++) {
            memcpy(a, nums, n * sizeof(int));
            int cur = i, d = dirs[di];
            while (cur >= 0 && cur < n) {
                if (a[cur] == 0) cur += d;
                else { a[cur]--; d = -d; cur += d; }
            }
            int ok = 1;
            for (int j = 0; j < n; j++) if (a[j] != 0) { ok = 0; break; }
            if (ok) ans++;
        }
    }
    free(a);
    return ans;
}
