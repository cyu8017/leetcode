// LeetCode 1502 - Can Make Arithmetic Progression From Sequence
// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

#include <stdlib.h>
#include <stdbool.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

bool canMakeArithmeticProgression(int* arr, int arrSize) {
    qsort(arr, (size_t)arrSize, sizeof(int), cmpInt);
    int diff = arr[1] - arr[0];
    for (int i = 2; i < arrSize; i++) {
        if (arr[i] - arr[i - 1] != diff) return false;
    }
    return true;
}
