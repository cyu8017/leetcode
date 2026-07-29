// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

#include <stdlib.h>

typedef struct {
    int key;
    int value;
    int used;
} SumEntry;

static unsigned int hashInt(int key, int capacity) {
    unsigned int x = (unsigned int)key;
    x ^= x >> 16;
    x *= 0x7feb352du;
    x ^= x >> 15;
    return x % (unsigned int)capacity;
}

static void sumAdd(SumEntry* table, int capacity, int key) {
    unsigned int idx = hashInt(key, capacity);
    while (table[idx].used && table[idx].key != key) {
        idx = (idx + 1) % (unsigned int)capacity;
    }
    if (!table[idx].used) {
        table[idx].used = 1;
        table[idx].key = key;
        table[idx].value = 0;
    }
    table[idx].value++;
}

static int sumGet(SumEntry* table, int capacity, int key) {
    unsigned int idx = hashInt(key, capacity);
    while (table[idx].used) {
        if (table[idx].key == key) {
            return table[idx].value;
        }
        idx = (idx + 1) % (unsigned int)capacity;
    }
    return 0;
}

int fourSumCount(int* nums1, int nums1Size, int* nums2, int nums2Size, int* nums3, int nums3Size, int* nums4, int nums4Size) {
    int capacity = nums1Size * nums2Size * 2 + 7;
    SumEntry* table = (SumEntry*)calloc((size_t)capacity, sizeof(SumEntry));
    for (int i = 0; i < nums1Size; i++) {
        for (int j = 0; j < nums2Size; j++) {
            sumAdd(table, capacity, nums1[i] + nums2[j]);
        }
    }

    int total = 0;
    for (int i = 0; i < nums3Size; i++) {
        for (int j = 0; j < nums4Size; j++) {
            total += sumGet(table, capacity, -(nums3[i] + nums4[j]));
        }
    }
    free(table);
    return total;
}
