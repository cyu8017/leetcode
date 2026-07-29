// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

#include <stdlib.h>

typedef struct {
    int* q;
    int head, tail, capacity;
} RecentCounter;

RecentCounter* recentCounterCreate(void) {
    RecentCounter* obj = (RecentCounter*)malloc(sizeof(RecentCounter));
    obj->capacity = 10001;
    obj->q = (int*)malloc((size_t)obj->capacity * sizeof(int));
    obj->head = obj->tail = 0;
    return obj;
}

int recentCounterPing(RecentCounter* obj, int t) {
    obj->q[obj->tail++] = t;
    while (obj->q[obj->head] < t - 3000) obj->head++;
    return obj->tail - obj->head;
}

void recentCounterFree(RecentCounter* obj) {
    free(obj->q);
    free(obj);
}
