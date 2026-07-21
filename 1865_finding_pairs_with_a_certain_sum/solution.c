// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int key;
    int value;
    bool used;
} HashEntry;

typedef struct {
    int* nums1;
    int nums1Size;
    int* nums2;
    int nums2Size;
    HashEntry* entries;
    int entryCapacity;
    int entryCount;
} FindSumPairs;

static unsigned int hashKey(int key) {
    return (unsigned int)key * 2654435761u;
}

static int findEntry(FindSumPairs* obj, int key, bool create) {
    unsigned int hash = hashKey(key);
    int index = (int)(hash & (unsigned int)(obj->entryCapacity - 1));
    for (;;) {
        if (!obj->entries[index].used) {
            if (create) {
                obj->entries[index].used = true;
                obj->entries[index].key = key;
                obj->entries[index].value = 0;
                obj->entryCount++;
                return index;
            }
            return -1;
        }
        if (obj->entries[index].key == key) return index;
        index = (index + 1) & (obj->entryCapacity - 1);
    }
}

static void resizeEntries(FindSumPairs* obj) {
    int oldCapacity = obj->entryCapacity;
    HashEntry* oldEntries = obj->entries;
    obj->entryCapacity *= 2;
    obj->entries = (HashEntry*)calloc((size_t)obj->entryCapacity, sizeof(HashEntry));
    obj->entryCount = 0;
    for (int i = 0; i < oldCapacity; i++) {
        if (oldEntries[i].used && oldEntries[i].value != 0) {
            int slot = findEntry(obj, oldEntries[i].key, true);
            obj->entries[slot].value = oldEntries[i].value;
        }
    }
    free(oldEntries);
}

static void mapAdd(FindSumPairs* obj, int key, int delta) {
    if (obj->entryCount * 2 >= obj->entryCapacity) resizeEntries(obj);
    int slot = findEntry(obj, key, true);
    obj->entries[slot].value += delta;
}

static int mapGet(FindSumPairs* obj, int key) {
    int slot = findEntry(obj, key, false);
    return slot < 0 ? 0 : obj->entries[slot].value;
}

FindSumPairs* findSumPairsCreate(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    FindSumPairs* obj = (FindSumPairs*)calloc(1, sizeof(FindSumPairs));
    obj->nums1Size = nums1Size;
    obj->nums2Size = nums2Size;
    obj->nums1 = (int*)malloc((size_t)nums1Size * sizeof(int));
    obj->nums2 = (int*)malloc((size_t)nums2Size * sizeof(int));
    memcpy(obj->nums1, nums1, (size_t)nums1Size * sizeof(int));
    memcpy(obj->nums2, nums2, (size_t)nums2Size * sizeof(int));
    obj->entryCapacity = 1;
    while (obj->entryCapacity < nums2Size * 4 + 16) obj->entryCapacity <<= 1;
    obj->entries = (HashEntry*)calloc((size_t)obj->entryCapacity, sizeof(HashEntry));
    for (int i = 0; i < nums2Size; i++) mapAdd(obj, nums2[i], 1);
    return obj;
}

void findSumPairsAdd(FindSumPairs* obj, int index, int val) {
    mapAdd(obj, obj->nums2[index], -1);
    obj->nums2[index] += val;
    mapAdd(obj, obj->nums2[index], 1);
}

int findSumPairsCount(FindSumPairs* obj, int tot) {
    int answer = 0;
    for (int i = 0; i < obj->nums1Size; i++) {
        answer += mapGet(obj, tot - obj->nums1[i]);
    }
    return answer;
}

void findSumPairsFree(FindSumPairs* obj) {
    if (!obj) return;
    free(obj->nums1);
    free(obj->nums2);
    free(obj->entries);
    free(obj);
}
