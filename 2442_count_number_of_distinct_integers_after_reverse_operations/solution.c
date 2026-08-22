// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

#include <stdlib.h>
#include <string.h>

static int rev2442(int x) {
    int r = 0;
    while (x > 0) {
        r = r * 10 + x % 10;
        x /= 10;
    }
    return r;
}

static int cmp_int(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int countDistinctIntegers(int* nums, int numsSize) {
    int* arr = (int*)malloc((size_t)numsSize * 2 * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        arr[i] = nums[i];
        arr[numsSize + i] = rev2442(nums[i]);
    }
    int m = numsSize * 2;
    qsort(arr, (size_t)m, sizeof(int), cmp_int);
    int cnt = 0;
    for (int i = 0; i < m; i++) {
        if (i == 0 || arr[i] != arr[i - 1]) cnt++;
    }
    free(arr);
    return cnt;
}
