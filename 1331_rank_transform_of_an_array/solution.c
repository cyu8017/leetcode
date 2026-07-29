// LeetCode 1331 - Rank Transform of an Array
// https://leetcode.com/problems/rank-transform-of-an-array/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int* arrayRankTransform(int* arr, int arrSize, int* returnSize) {
    int* sorted = (int*)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) sorted[i] = arr[i];
    qsort(sorted, arrSize, sizeof(int), cmp_int);
    int uniq = 0;
    for (int i = 0; i < arrSize; i++)
        if (i == 0 || sorted[i] != sorted[i - 1]) sorted[uniq++] = sorted[i];
    int* ans = (int*)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) {
        int lo = 0, hi = uniq - 1, rank = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (sorted[mid] == arr[i]) { rank = mid + 1; break; }
            if (sorted[mid] < arr[i]) lo = mid + 1;
            else hi = mid - 1;
        }
        ans[i] = rank;
    }
    free(sorted);
    *returnSize = arrSize;
    return ans;
}
