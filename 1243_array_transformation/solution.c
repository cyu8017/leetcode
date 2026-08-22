// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

#include <stdlib.h>
#include <string.h>

int* transformArray(int* arr, int arrSize, int* returnSize) {
    int* cur = (int*)malloc((size_t)arrSize * sizeof(int));
    memcpy(cur, arr, (size_t)arrSize * sizeof(int));
    for (;;) {
        int* nxt = (int*)malloc((size_t)arrSize * sizeof(int));
        memcpy(nxt, cur, (size_t)arrSize * sizeof(int));
        for (int i = 1; i + 1 < arrSize; i++) {
            if (cur[i] < cur[i - 1] && cur[i] < cur[i + 1]) nxt[i]++;
            else if (cur[i] > cur[i - 1] && cur[i] > cur[i + 1]) nxt[i]--;
        }
        int same = 1;
        for (int i = 0; i < arrSize; i++) {
            if (nxt[i] != cur[i]) {
                same = 0;
                break;
            }
        }
        if (same) {
            free(nxt);
            break;
        }
        free(cur);
        cur = nxt;
    }
    *returnSize = arrSize;
    return cur;
}
