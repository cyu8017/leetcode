// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

#include <stdlib.h>

typedef struct {
    int key;
    int value;
    int used;
} HashEntry;

static unsigned int hashInt(int key, int capacity) {
    unsigned int x = (unsigned int)key;
    x ^= x >> 16;
    x *= 0x7feb352du;
    x ^= x >> 15;
    return x % (unsigned int)capacity;
}

static void hashPut(HashEntry* table, int capacity, int key, int delta) {
    unsigned int idx = hashInt(key, capacity);
    while (table[idx].used && table[idx].key != key) {
        idx = (idx + 1) % (unsigned int)capacity;
    }
    if (!table[idx].used) {
        table[idx].used = 1;
        table[idx].key = key;
        table[idx].value = 0;
    }
    table[idx].value += delta;
}

static int hashGet(HashEntry* table, int capacity, int key) {
    unsigned int idx = hashInt(key, capacity);
    while (table[idx].used) {
        if (table[idx].key == key) {
            return table[idx].value;
        }
        idx = (idx + 1) % (unsigned int)capacity;
    }
    return 0;
}

int subarraySum(int* nums, int numsSize, int k) {
    int capacity = numsSize * 2 + 7;
    HashEntry* table = (HashEntry*)calloc((size_t)capacity, sizeof(HashEntry));
    hashPut(table, capacity, 0, 1);
    int prefix = 0;
    int total = 0;
    for (int i = 0; i < numsSize; i++) {
        prefix += nums[i];
        total += hashGet(table, capacity, prefix - k);
        hashPut(table, capacity, prefix, 1);
    }
    free(table);
    return total;
}
