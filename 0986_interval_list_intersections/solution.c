// LeetCode 0986 - Interval List Intersections
// https://leetcode.com/problems/interval-list-intersections/

#include <stdlib.h>

int** intervalIntersection(int** firstList, int firstListSize, int* firstListColSize, int** secondList, int secondListSize, int* secondListColSize, int* returnSize, int** returnColumnSizes) {
    (void)firstListColSize; (void)secondListColSize;
    int cap = firstListSize + secondListSize;
    int** ans = (int**)malloc((size_t)cap * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)cap * sizeof(int));
    int n = 0, i = 0, j = 0;
    while (i < firstListSize && j < secondListSize) {
        int lo = firstList[i][0] > secondList[j][0] ? firstList[i][0] : secondList[j][0];
        int hi = firstList[i][1] < secondList[j][1] ? firstList[i][1] : secondList[j][1];
        if (lo <= hi) {
            ans[n] = (int*)malloc(2 * sizeof(int));
            ans[n][0] = lo; ans[n][1] = hi;
            (*returnColumnSizes)[n] = 2;
            n++;
        }
        if (firstList[i][1] < secondList[j][1]) i++; else j++;
    }
    *returnSize = n;
    return ans;
}
