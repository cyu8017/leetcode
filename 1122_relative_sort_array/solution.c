// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

#include <stdlib.h>
#include <string.h>

int* relativeSortArray(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize) {
    int count[1001];
    memset(count, 0, sizeof(count));
    for (int i = 0; i < arr1Size; i++) count[arr1[i]]++;
    int* ans = (int*)malloc((size_t)arr1Size * sizeof(int));
    int idx = 0;
    for (int i = 0; i < arr2Size; i++) {
        int x = arr2[i];
        while (count[x] > 0) { ans[idx++] = x; count[x]--; }
    }
    for (int x = 0; x <= 1000; x++) {
        while (count[x] > 0) { ans[idx++] = x; count[x]--; }
    }
    *returnSize = arr1Size;
    return ans;
}
