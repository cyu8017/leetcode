// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

#include <stdlib.h>

typedef struct {
    int* stack;
    int* maxes;
    int size;
    int capacity;
} MaxStack;

MaxStack* maxStackCreate(void) {
    MaxStack* obj = (MaxStack*)calloc(1, sizeof(MaxStack));
    return obj;
}

static void ensure(MaxStack* obj) {
    if (obj->size < obj->capacity) {
        return;
    }
    obj->capacity = obj->capacity ? obj->capacity * 2 : 8;
    obj->stack = (int*)realloc(obj->stack, (size_t)obj->capacity * sizeof(int));
    obj->maxes = (int*)realloc(obj->maxes, (size_t)obj->capacity * sizeof(int));
}

void maxStackPush(MaxStack* obj, int x) {
    ensure(obj);
    obj->stack[obj->size] = x;
    obj->maxes[obj->size] = obj->size == 0 || x > obj->maxes[obj->size - 1] ? x : obj->maxes[obj->size - 1];
    obj->size++;
}

int maxStackPop(MaxStack* obj) {
    return obj->stack[--obj->size];
}

int maxStackTop(MaxStack* obj) {
    return obj->stack[obj->size - 1];
}

int maxStackPeekMax(MaxStack* obj) {
    return obj->maxes[obj->size - 1];
}

int maxStackPopMax(MaxStack* obj) {
    int maxVal = maxStackPeekMax(obj);
    int* buffer = (int*)malloc((size_t)obj->size * sizeof(int));
    int b = 0;
    while (maxStackTop(obj) != maxVal) {
        buffer[b++] = maxStackPop(obj);
    }
    maxStackPop(obj);
    while (b > 0) {
        maxStackPush(obj, buffer[--b]);
    }
    free(buffer);
    return maxVal;
}

void maxStackFree(MaxStack* obj) {
    free(obj->stack);
    free(obj->maxes);
    free(obj);
}
