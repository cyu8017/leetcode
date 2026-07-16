// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

#include <stdlib.h>

typedef struct {
    int key;
    int value;
} Entry;

static int lookup(const Entry* entries, int size, int key) {
    for (int index = 0; index < size; index++) {
        if (entries[index].key == key) {
            return entries[index].value;
        }
    }
    return -1;
}

int* nextGreaterElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    Entry entries[2000];
    int entryCount = 0;
    int stack[2000];
    int top = 0;

    for (int index = 0; index < nums2Size; index++) {
        const int num = nums2[index];
        while (top > 0 && stack[top - 1] < num) {
            entries[entryCount].key = stack[--top];
            entries[entryCount++].value = num;
        }
        stack[top++] = num;
    }

    int* result = (int*)malloc((size_t)nums1Size * sizeof(int));
    for (int index = 0; index < nums1Size; index++) {
        result[index] = lookup(entries, entryCount, nums1[index]);
    }
    *returnSize = nums1Size;
    return result;
}
