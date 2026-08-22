// LeetCode 0325 - Maximum Size Subarray Sum Equals k
// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

#include <stdlib.h>

typedef struct {
    long long key;
    int value;
    int used;
} HashEntry;

static unsigned long long hashKey(long long key) {
    unsigned long long value = (unsigned long long)key;
    value ^= (unsigned long long)(key >> 33);
    value *= 0xff51afd7ed558ccdULL;
    value ^= value >> 33;
    return value;
}

static int hashLookup(HashEntry* table, int capacity, long long key, int* found) {
    unsigned long long hash = hashKey(key);
    int index = (int)(hash & (unsigned long long)(capacity - 1));
    for (int probe = 0; probe < capacity; probe++) {
        if (!table[index].used) {
            *found = 0;
            return index;
        }
        if (table[index].key == key) {
            *found = 1;
            return index;
        }
        index = (index + 1) & (capacity - 1);
    }
    *found = 0;
    return -1;
}

int maxSubArrayLen(int* nums, int numsSize, int k) {
    int capacity = 16;
    HashEntry* table = (HashEntry*)calloc((size_t)capacity, sizeof(HashEntry));
    int found = 0;
    int slot = hashLookup(table, capacity, 0, &found);
    table[slot].key = 0;
    table[slot].value = -1;
    table[slot].used = 1;

    long long prefix = 0;
    int best = 0;
    for (int index = 0; index < numsSize; index++) {
        prefix += nums[index];
        int targetFound = 0;
        int targetSlot = hashLookup(table, capacity, prefix - k, &targetFound);
        if (targetFound) {
            int length = index - table[targetSlot].value;
            if (length > best) {
                best = length;
            }
        }
        int prefixFound = 0;
        int prefixSlot = hashLookup(table, capacity, prefix, &prefixFound);
        if (!prefixFound) {
            if (table[prefixSlot].used) {
                HashEntry* newTable = (HashEntry*)calloc((size_t)(capacity * 2), sizeof(HashEntry));
                for (int entry = 0; entry < capacity; entry++) {
                    if (table[entry].used) {
                        int insertFound = 0;
                        int insertSlot = hashLookup(newTable, capacity * 2, table[entry].key, &insertFound);
                        newTable[insertSlot] = table[entry];
                    }
                }
                free(table);
                table = newTable;
                capacity *= 2;
                prefixSlot = hashLookup(table, capacity, prefix, &prefixFound);
            }
            table[prefixSlot].key = prefix;
            table[prefixSlot].value = index;
            table[prefixSlot].used = 1;
        }
    }

    free(table);
    return best;
}
