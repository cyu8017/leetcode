// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

#include <stdlib.h>

int* pancakeSort(int* arr, int arrSize, int* returnSize) {
    int* a = (int*)malloc((size_t)arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) a[i] = arr[i];
    int* ans = (int*)malloc((size_t)(arrSize * 2) * sizeof(int));
    int an = 0;
    for (int size = arrSize; size > 1; size--) {
        int i = 0;
        while (a[i] != size) i++;
        if (i == size - 1) continue;
        if (i) {
            ans[an++] = i + 1;
            for (int L = 0, R = i; L < R; L++, R--) { int t=a[L]; a[L]=a[R]; a[R]=t; }
        }
        ans[an++] = size;
        for (int L = 0, R = size - 1; L < R; L++, R--) { int t=a[L]; a[L]=a[R]; a[R]=t; }
    }
    free(a);
    *returnSize = an;
    return ans;
}
