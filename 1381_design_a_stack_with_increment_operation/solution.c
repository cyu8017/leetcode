// LeetCode 1381 - Design a Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

#include <stdlib.h>

typedef struct {
    int* a;
    int size;
    int maxSize;
} CustomStack;

CustomStack* customStackCreate(int maxSize) {
    CustomStack* obj = (CustomStack*)malloc(sizeof(CustomStack));
    obj->maxSize = maxSize;
    obj->size = 0;
    obj->a = (int*)malloc(maxSize * sizeof(int));
    return obj;
}

void customStackPush(CustomStack* obj, int x) {
    if (obj->size < obj->maxSize) obj->a[obj->size++] = x;
}

int customStackPop(CustomStack* obj) {
    if (!obj->size) return -1;
    return obj->a[--obj->size];
}

void customStackIncrement(CustomStack* obj, int k, int val) {
    int lim = k < obj->size ? k : obj->size;
    for (int i = 0; i < lim; i++) obj->a[i] += val;
}

void customStackFree(CustomStack* obj) {
    free(obj->a);
    free(obj);
}
