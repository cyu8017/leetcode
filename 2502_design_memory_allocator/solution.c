// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int* mem;
    int n;
} Allocator;

Allocator* allocatorCreate(int n) {
    Allocator* obj = (Allocator*)malloc(sizeof(Allocator));
    obj->n = n;
    obj->mem = (int*)calloc((size_t)n, sizeof(int));
    return obj;
}

int allocatorAllocate(Allocator* obj, int size, int mID) {
    int freeCnt = 0;
    for (int i = 0; i < obj->n; i++) {
        if (obj->mem[i] == 0) {
            freeCnt++;
            if (freeCnt == size) {
                int start = i - size + 1;
                for (int j = start; j <= i; j++) obj->mem[j] = mID;
                return start;
            }
        } else freeCnt = 0;
    }
    return -1;
}

int allocatorFreeMemory(Allocator* obj, int mID) {
    int cnt = 0;
    for (int i = 0; i < obj->n; i++) {
        if (obj->mem[i] == mID) { obj->mem[i] = 0; cnt++; }
    }
    return cnt;
}

void allocatorFree(Allocator* obj) {
    free(obj->mem);
    free(obj);
}
