// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

#include <stdlib.h>
#include <string.h>

static int solve2459(int* nums, int n, int startZero) {
    int* arr = (int*)malloc((size_t)n * sizeof(int));
    int* pos = (int*)malloc((size_t)n * sizeof(int));
    memcpy(arr, nums, (size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) pos[arr[i]] = i;
    int ops = 0;
    for (;;) {
        int empty = pos[0];
        int should;
        if (startZero) should = empty;
        else should = (empty == n - 1) ? 0 : empty + 1;
        if (arr[empty] == should) {
            int found = -1;
            for (int i = 0; i < n; i++) {
                int want = startZero ? i : (i == n - 1 ? 0 : i + 1);
                if (arr[i] != want) { found = i; break; }
            }
            if (found == -1) { free(arr); free(pos); return ops; }
            int v = arr[found];
            arr[empty] = arr[found];
            arr[found] = 0;
            pos[0] = found;
            pos[v] = empty;
            ops++;
            continue;
        }
        int j = pos[should];
        int v = arr[j];
        arr[empty] = arr[j];
        arr[j] = 0;
        pos[0] = j;
        pos[v] = empty;
        ops++;
    }
}

int sortArray(int* nums, int numsSize) {
    int a = solve2459(nums, numsSize, 1);
    int b = solve2459(nums, numsSize, 0);
    return a < b ? a : b;
}
