// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

#include <stdlib.h>

int* timeTaken(int* arrival, int arrivalSize, int* state, int stateSize, int* returnSize) {
    (void)stateSize;
    int n = arrivalSize;
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int* enter = (int*)malloc((size_t)n * sizeof(int));
    int* exitq = (int*)malloc((size_t)n * sizeof(int));
    int eh = 0, et = 0, xh = 0, xt = 0;
    int i = 0, t = 0, prev = 1;
    while (i < n || eh < et || xh < xt) {
        while (i < n && arrival[i] <= t) {
            if (state[i] == 0) enter[et++] = i;
            else exitq[xt++] = i;
            i++;
        }
        if (eh == et && xh == xt) {
            if (i < n) { t = arrival[i]; prev = 1; }
            continue;
        }
        if (prev == 1) {
            if (xh < xt) { ans[exitq[xh++]] = t; prev = 1; }
            else { ans[enter[eh++]] = t; prev = 0; }
        } else {
            if (eh < et) { ans[enter[eh++]] = t; prev = 0; }
            else { ans[exitq[xh++]] = t; prev = 1; }
        }
        t++;
    }
    free(enter); free(exitq);
    *returnSize = n;
    return ans;
}
