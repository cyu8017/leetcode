// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

#include <stdlib.h>

typedef struct {
    int key;
    int count;
} FreqEntry;

static int compare_freq_entries(const void* left, const void* right) {
    const FreqEntry* a = (const FreqEntry*)left;
    const FreqEntry* b = (const FreqEntry*)right;
    return a->key - b->key;
}

static int find_freq(FreqEntry* entries, int size, int key) {
    for (int index = 0; index < size; index++) {
        if (entries[index].key == key) {
            return entries[index].count;
        }
    }
    return 0;
}

int findPairs(int* nums, int numsSize, int k) {
    if (k < 0) {
        return 0;
    }

    FreqEntry* entries = (FreqEntry*)malloc((size_t)numsSize * sizeof(FreqEntry));
    if (!entries) {
        return 0;
    }

    int size = 0;
    for (int index = 0; index < numsSize; index++) {
        const int key = nums[index];
        int found = 0;
        for (int entryIndex = 0; entryIndex < size; entryIndex++) {
            if (entries[entryIndex].key == key) {
                entries[entryIndex].count++;
                found = 1;
                break;
            }
        }
        if (!found) {
            entries[size].key = key;
            entries[size].count = 1;
            size++;
        }
    }

    int pairs = 0;
    for (int index = 0; index < size; index++) {
        const int num = entries[index].key;
        if (k == 0) {
            if (entries[index].count > 1) {
                pairs++;
            }
        } else if (find_freq(entries, size, num + k) > 0) {
            pairs++;
        }
    }

    free(entries);
    return pairs;
}
