// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

#include <stdbool.h>
#include <stdlib.h>

typedef struct BucketNode {
    long long key;
    long long value;
    struct BucketNode* next;
} BucketNode;

static long long bucketId(long long num, long long width) {
    return num >= 0 ? num / width : (num + 1) / width - 1;
}

static long long absLong(long long value) {
    return value < 0 ? -value : value;
}

static BucketNode** createTable(int size) {
    return (BucketNode**)calloc((size_t)size, sizeof(BucketNode*));
}

static void freeTable(BucketNode** table, int size) {
    for (int i = 0; i < size; i++) {
        BucketNode* node = table[i];
        while (node) {
            BucketNode* next = node->next;
            free(node);
            node = next;
        }
    }
    free(table);
}

static bool tableContains(BucketNode** table, int size, long long key, long long* value) {
    int index = (int)(key % size);
    if (index < 0) {
        index += size;
    }
    BucketNode* node = table[index];
    while (node) {
        if (node->key == key) {
            *value = node->value;
            return true;
        }
        node = node->next;
    }
    return false;
}

static void tablePut(BucketNode** table, int size, long long key, long long value) {
    int index = (int)(key % size);
    if (index < 0) {
        index += size;
    }
    BucketNode* node = table[index];
    while (node) {
        if (node->key == key) {
            node->value = value;
            return;
        }
        node = node->next;
    }
    BucketNode* newNode = (BucketNode*)malloc(sizeof(BucketNode));
    newNode->key = key;
    newNode->value = value;
    newNode->next = table[index];
    table[index] = newNode;
}

static void tableRemove(BucketNode** table, int size, long long key) {
    int index = (int)(key % size);
    if (index < 0) {
        index += size;
    }
    BucketNode* node = table[index];
    BucketNode* prev = NULL;
    while (node) {
        if (node->key == key) {
            if (prev) {
                prev->next = node->next;
            } else {
                table[index] = node->next;
            }
            free(node);
            return;
        }
        prev = node;
        node = node->next;
    }
}

static int tableSize(BucketNode** table, int size) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        BucketNode* node = table[i];
        while (node) {
            count++;
            node = node->next;
        }
    }
    return count;
}

bool containsNearbyAlmostDuplicate(int* nums, int numsSize, int indexDiff, int valueDiff) {
    if (indexDiff <= 0 || valueDiff < 0) {
        return false;
    }
    long long width = (long long)valueDiff + 1;
    const int tableSizeValue = 4096;
    BucketNode** table = createTable(tableSizeValue);

    for (int i = 0; i < numsSize; i++) {
        long long num = nums[i];
        long long bucket = bucketId(num, width);
        long long existing = 0;

        if (tableContains(table, tableSizeValue, bucket, &existing)) {
            freeTable(table, tableSizeValue);
            return true;
        }
        if (tableContains(table, tableSizeValue, bucket - 1, &existing)
            && absLong(num - existing) <= valueDiff) {
            freeTable(table, tableSizeValue);
            return true;
        }
        if (tableContains(table, tableSizeValue, bucket + 1, &existing)
            && absLong(num - existing) <= valueDiff) {
            freeTable(table, tableSizeValue);
            return true;
        }
        if (tableSize(table, tableSizeValue) >= indexDiff) {
            long long old = nums[i - indexDiff];
            tableRemove(table, tableSizeValue, bucketId(old, width));
        }
        tablePut(table, tableSizeValue, bucket, num);
    }

    freeTable(table, tableSizeValue);
    return false;
}
