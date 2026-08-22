// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

#include <stdlib.h>
#include <string.h>

typedef struct {
    long long key;
    int value;
    int used;
} DiffEntry;

static unsigned int hashLL(long long key, int capacity) {
    unsigned long long x = (unsigned long long)key;
    x ^= x >> 33;
    x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33;
    return (unsigned int)(x % (unsigned int)capacity);
}

static void diffAdd(DiffEntry* table, int capacity, long long key, int delta) {
    unsigned int idx = hashLL(key, capacity);
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

static int diffGet(DiffEntry* table, int capacity, long long key) {
    unsigned int idx = hashLL(key, capacity);
    while (table[idx].used) {
        if (table[idx].key == key) {
            return table[idx].value;
        }
        idx = (idx + 1) % (unsigned int)capacity;
    }
    return 0;
}

int numberOfArithmeticSlices(int* nums, int numsSize) {
    int capacity = numsSize * 4 + 7;
    DiffEntry** tables = (DiffEntry**)malloc((size_t)numsSize * sizeof(DiffEntry*));
    for (int i = 0; i < numsSize; i++) {
        tables[i] = (DiffEntry*)calloc((size_t)capacity, sizeof(DiffEntry));
    }

    int total = 0;
    for (int index = 0; index < numsSize; index++) {
        for (int previous = 0; previous < index; previous++) {
            long long diff = (long long)nums[index] - nums[previous];
            int count = diffGet(tables[previous], capacity, diff);
            total += count;
            diffAdd(tables[index], capacity, diff, count + 1);
        }
    }

    for (int i = 0; i < numsSize; i++) {
        free(tables[i]);
    }
    free(tables);
    return total;
}
