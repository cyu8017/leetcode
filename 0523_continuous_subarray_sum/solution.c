// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

#include <stdbool.h>
#include <stdlib.h>

typedef struct Entry {
    long long key;
    int value;
    struct Entry* next;
} Entry;

static Entry* mapGet(Entry** buckets, int bucketCount, long long key) {
    const int bucket = (int)((key % bucketCount + bucketCount) % bucketCount);
    for (Entry* entry = buckets[bucket]; entry; entry = entry->next) {
        if (entry->key == key) {
            return entry;
        }
    }
    return NULL;
}

static void mapSet(Entry** buckets, int bucketCount, long long key, int value) {
    const int bucket = (int)((key % bucketCount + bucketCount) % bucketCount);
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

bool checkSubarraySum(int* nums, int numsSize, int k) {
    long long prefix = 0;
    const int bucketCount = 4096;
    Entry** buckets = (Entry**)calloc((size_t)bucketCount, sizeof(Entry*));
    mapSet(buckets, bucketCount, 0, -1);

    for (int index = 0; index < numsSize; index++) {
        prefix += nums[index];
        const long long mod = k != 0 ? prefix % k : prefix;
        Entry* found = mapGet(buckets, bucketCount, mod);
        if (found) {
            if (index - found->value >= 2) {
                mapFree(buckets, bucketCount);
                return true;
            }
        } else {
            mapSet(buckets, bucketCount, mod, index);
        }
    }

    mapFree(buckets, bucketCount);
    return false;
}
