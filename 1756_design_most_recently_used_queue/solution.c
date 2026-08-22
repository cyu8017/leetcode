// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int* q;
    int size;
} MRUQueue;

MRUQueue* mRUQueueCreate(int n) {
    MRUQueue* obj = (MRUQueue*) malloc(sizeof(MRUQueue));
    obj->q = (int*) malloc(n * sizeof(int));
    obj->size = n;
    for (int i = 0; i < n; i++) {
        obj->q[i] = i + 1;
    }
    return obj;
}

int mRUQueueFetch(MRUQueue* obj, int k) {
    int val = obj->q[k - 1];
    memmove(obj->q + k - 1, obj->q + k, (obj->size - k) * sizeof(int));
    obj->q[obj->size - 1] = val;
    return val;
}

void mRUQueueFree(MRUQueue* obj) {
    free(obj->q);
    free(obj);
}
