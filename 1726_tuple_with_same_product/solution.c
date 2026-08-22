// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

#include <stdlib.h>

int tupleSameProduct(int* nums, int numsSize) {
    int pairCount = numsSize * (numsSize - 1) / 2;
    int capacity = 8;
    while (capacity < pairCount * 2) {
        capacity <<= 1;
    }
    long long* keys = (long long*)calloc(capacity, sizeof(long long));
    int* counts = (int*)calloc(capacity, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            long long product = (long long)nums[i] * nums[j];
            int slot = (int)(product & (capacity - 1));
            while (keys[slot] != 0 && keys[slot] != product) {
                slot = (slot + 1) & (capacity - 1);
            }
            keys[slot] = product;
            counts[slot]++;
        }
    }
    long long result = 0;
    for (int slot = 0; slot < capacity; slot++) {
        if (counts[slot] > 0) {
            result += (long long)counts[slot] * (counts[slot] - 1) * 4;
        }
    }
    free(keys);
    free(counts);
    return (int)result;
}
