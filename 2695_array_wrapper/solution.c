// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    int* nums;
    int size;
} ArrayWrapper;

ArrayWrapper* arrayWrapperCreate(int* nums, int numsSize) {
    ArrayWrapper* a = (ArrayWrapper*)malloc(sizeof(ArrayWrapper));
    a->size = numsSize;
    a->nums = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) a->nums[i] = nums[i];
    return a;
}

int arrayWrapperValueOf(ArrayWrapper* a) {
    int s = 0;
    for (int i = 0; i < a->size; i++) s += a->nums[i];
    return s;
}

char* arrayWrapperToString(ArrayWrapper* a) {
    char* buf = (char*)malloc((size_t)a->size * 16 + 4);
    char* p = buf;
    *p++ = '[';
    for (int i = 0; i < a->size; i++) {
        if (i) *p++ = ',';
        p += sprintf(p, "%d", a->nums[i]);
    }
    *p++ = ']';
    *p = '\0';
    return buf;
}

void arrayWrapperFree(ArrayWrapper* a) {
    if (!a) return;
    free(a->nums);
    free(a);
}
