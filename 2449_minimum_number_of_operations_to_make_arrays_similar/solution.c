// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

long long makeSimilar(int* nums, int numsSize, int* target, int targetSize) {
    (void)targetSize;
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    qsort(target, (size_t)numsSize, sizeof(int), cmp_int);
    int* oddN = (int*)malloc((size_t)numsSize * sizeof(int));
    int* evenN = (int*)malloc((size_t)numsSize * sizeof(int));
    int* oddT = (int*)malloc((size_t)numsSize * sizeof(int));
    int* evenT = (int*)malloc((size_t)numsSize * sizeof(int));
    int on = 0, en = 0, ot = 0, et = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0) evenN[en++] = nums[i];
        else oddN[on++] = nums[i];
        if (target[i] % 2 == 0) evenT[et++] = target[i];
        else oddT[ot++] = target[i];
    }
    long long ans = 0;
    for (int i = 0; i < on; i++) {
        int diff = oddN[i] - oddT[i];
        if (diff > 0) ans += diff / 2;
    }
    for (int i = 0; i < en; i++) {
        int diff = evenN[i] - evenT[i];
        if (diff > 0) ans += diff / 2;
    }
    free(oddN); free(evenN); free(oddT); free(evenT);
    return ans;
}
