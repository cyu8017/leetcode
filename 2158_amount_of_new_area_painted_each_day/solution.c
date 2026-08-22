// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

#include <stdlib.h>
#include <string.h>

int* amountPainted(int** paint, int paintSize, int* paintColSize, int* returnSize) {
    (void)paintColSize;
    int* ans = (int*)calloc((size_t)paintSize, sizeof(int));
    int* line = (int*)calloc(50001, sizeof(int));
    for (int i = 0; i < paintSize; i++) {
        int start = paint[i][0], end = paint[i][1];
        int j = start;
        while (j < end) {
            if (line[j] == 0) {
                ans[i]++;
                line[j] = end;
                j++;
            } else {
                int next = line[j];
                line[j] = end > next ? end : next;
                j = next;
            }
        }
    }
    free(line);
    *returnSize = paintSize;
    return ans;
}
