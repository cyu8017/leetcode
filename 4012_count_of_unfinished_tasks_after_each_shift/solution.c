// LeetCode 4012 - Count Of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

#include <stdlib.h>
#include <stdint.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countTasks(int* tasks, int tasksSize, int* shifts, int shiftsSize, int* returnSize) {
    int m = tasksSize, n = shiftsSize;
    int64_t* s = (int64_t*)malloc((size_t)(m + 1) * sizeof(int64_t));
    s[0] = 0;
    for (int i = 0; i < m; i++) s[i + 1] = s[i] + (int64_t)tasks[i];

    int* ans = (int*)calloc((size_t)n, sizeof(int));
    int i = 0;
    int64_t cur = 0;

    for (int j = 0; j < n; j++) {
        if ((int64_t)shifts[j] < (int64_t)tasks[i] - cur) {
            cur += (int64_t)shifts[j];
            ans[j] = m - i;
        } else {
            int64_t t = (int64_t)shifts[j] - ((int64_t)tasks[i] - cur);
            if (t >= s[m] - s[i + 1]) {
                i = 0;
                cur = 0;
                /* ans[j] stays 0 */
            } else {
                int l = i + 1, r = m;
                while (l < r) {
                    int mid = (l + r) >> 1;
                    if (t < s[mid + 1] - s[i + 1]) r = mid;
                    else l = mid + 1;
                }
                cur = t - (s[l] - s[i + 1]);
                i = l;
                ans[j] = m - i;
            }
        }
    }

    free(s);
    *returnSize = n;
    return ans;
}
