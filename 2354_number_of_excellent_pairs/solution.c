// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

long long countExcellentPairs(int* nums, int numsSize, int k) {
    int* arr = (int*)malloc((size_t)numsSize * sizeof(int));
    memcpy(arr, nums, (size_t)numsSize * sizeof(int));
    qsort(arr, (size_t)numsSize, sizeof(int), cmpInt);
    int m = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i == 0 || arr[i] != arr[i - 1]) arr[m++] = arr[i];
    }
    int cnt[32] = {0};
    for (int i = 0; i < m; i++) {
        int bits = 0;
        for (unsigned y = (unsigned)arr[i]; y; y >>= 1) bits += (int)(y & 1);
        cnt[bits]++;
    }
    free(arr);
    long long ans = 0;
    for (int i = 0; i < 32; i++)
        for (int j = 0; j < 32; j++)
            if (i + j >= k) ans += (long long)cnt[i] * cnt[j];
    return ans;
}
