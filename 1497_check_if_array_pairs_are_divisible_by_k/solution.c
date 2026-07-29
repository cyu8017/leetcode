// LeetCode 1497 - Check If Array Pairs Are Divisible by k
// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

#include <stdbool.h>
#include <stdlib.h>

bool canArrange(int* arr, int arrSize, int k) {
    int* count = (int*)calloc(k, sizeof(int));
    for (int i = 0; i < arrSize; i++) {
        int r = arr[i] % k;
        if (r < 0) r += k;
        count[r]++;
    }
    if (count[0] % 2) { free(count); return false; }
    for (int r = 1; r < k; r++)
        if (count[r] != count[k - r]) { free(count); return false; }
    free(count);
    return true;
}
