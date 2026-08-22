// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

#include <stdlib.h>

typedef struct Entry {
    int key;
    int value;
    struct Entry* next;
} Entry;

static Entry* mapGet(Entry** buckets, int bucketCount, int key) {
    const int bucket = (key % bucketCount + bucketCount) % bucketCount;
    for (Entry* entry = buckets[bucket]; entry; entry = entry->next) {
        if (entry->key == key) {
            return entry;
        }
    }
    return NULL;
}

static void mapSet(Entry** buckets, int bucketCount, int key, int value) {
    const int bucket = (key % bucketCount + bucketCount) % bucketCount;
    for (Entry* entry = buckets[bucket]; entry; entry = entry->next) {
        if (entry->key == key) {
            return;
        }
    }
    Entry* entry = (Entry*)malloc(sizeof(Entry));
    entry->key = key;
    entry->value = value;
    entry->next = buckets[bucket];
    buckets[bucket] = entry;
}

static void mapFree(Entry** buckets, int bucketCount) {
    for (int index = 0; index < bucketCount; index++) {
        Entry* entry = buckets[index];
        while (entry) {
            Entry* next = entry->next;
            free(entry);
            entry = next;
        }
    }
    free(buckets);
}

int findMaxLength(int* nums, int numsSize) {
    const int bucketCount = 4096;
    Entry** buckets = (Entry**)calloc((size_t)bucketCount, sizeof(Entry*));
    mapSet(buckets, bucketCount, 0, -1);

    int balance = 0;
    int best = 0;
    for (int index = 0; index < numsSize; index++) {
        balance += nums[index] == 1 ? 1 : -1;
        Entry* found = mapGet(buckets, bucketCount, balance);
        if (found) {
            const int length = index - found->value;
            if (length > best) {
                best = length;
            }
        } else {
            mapSet(buckets, bucketCount, balance, index);
        }
    }

    mapFree(buckets, bucketCount);
    return best;
}
