// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* arraysIntersection(int* arr1, int arr1Size, int* arr2, int arr2Size, int* arr3, int arr3Size, int* returnSize) {
    int i = 0, j = 0, k = 0;
    int* tmp = (int*)malloc((size_t)(arr1Size < arr2Size ? arr1Size : arr2Size) * sizeof(int));
    int count = 0;
    while (i < arr1Size && j < arr2Size && k < arr3Size) {
        if (arr1[i] == arr2[j] && arr2[j] == arr3[k]) {
            tmp[count++] = arr1[i];
            i++;
            j++;
            k++;
        } else {
            int maxv = arr1[i];
            if (arr2[j] > maxv) maxv = arr2[j];
            if (arr3[k] > maxv) maxv = arr3[k];
            while (i < arr1Size && arr1[i] < maxv) i++;
            while (j < arr2Size && arr2[j] < maxv) j++;
            while (k < arr3Size && arr3[k] < maxv) k++;
        }
    }
    qsort(tmp, (size_t)count, sizeof(int), cmpInt);
    *returnSize = count;
    return tmp;
}
