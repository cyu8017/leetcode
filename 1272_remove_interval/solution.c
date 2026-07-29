// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 */
int** removeInterval(int** intervals, int intervalsSize, int* intervalsColSize, int* toBeRemoved, int toBeRemovedSize, int* returnSize, int** returnColumnSizes) {
    (void)intervalsColSize;
    (void)toBeRemovedSize;
    int left = toBeRemoved[0], right = toBeRemoved[1];
    int cap = intervalsSize * 2;
    int** ans = (int**)malloc((size_t)cap * sizeof(int*));
    int* colSizes = (int*)malloc((size_t)cap * sizeof(int));
    int count = 0;
    for (int i = 0; i < intervalsSize; i++) {
        int start = intervals[i][0], end = intervals[i][1];
        if (end <= left || start >= right) {
            ans[count] = (int*)malloc(2 * sizeof(int));
            ans[count][0] = start;
            ans[count][1] = end;
            colSizes[count] = 2;
            count++;
        } else {
            if (start < left) {
                ans[count] = (int*)malloc(2 * sizeof(int));
                ans[count][0] = start;
                ans[count][1] = left;
                colSizes[count] = 2;
                count++;
            }
            if (end > right) {
                ans[count] = (int*)malloc(2 * sizeof(int));
                ans[count][0] = right;
                ans[count][1] = end;
                colSizes[count] = 2;
                count++;
            }
        }
    }
    *returnSize = count;
    *returnColumnSizes = (int*)realloc(colSizes, (size_t)count * sizeof(int));
    ans = (int**)realloc(ans, (size_t)count * sizeof(int*));
    return ans;
}
