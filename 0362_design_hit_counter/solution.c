// LeetCode 0362 - Design Hit Counter
// https://leetcode.com/problems/design-hit-counter/

#include <stdlib.h>

typedef struct {
    int* hits;
    int count;
    int capacity;
} HitCounter;

HitCounter* hitCounterCreate() {
    HitCounter* obj = (HitCounter*)calloc(1, sizeof(HitCounter));
    obj->capacity = 16;
    obj->hits = (int*)malloc((size_t)obj->capacity * sizeof(int));
    return obj;
}

void hitCounterHit(HitCounter* obj, int timestamp) {
    if (obj->count >= obj->capacity) {
        obj->capacity *= 2;
        obj->hits = (int*)realloc(obj->hits, (size_t)obj->capacity * sizeof(int));
    }
    obj->hits[obj->count] = timestamp;
    obj->count += 1;
}

int hitCounterGetHits(HitCounter* obj, int timestamp) {
    while (obj->count > 0 && obj->hits[0] <= timestamp - 300) {
        for (int index = 1; index < obj->count; index++) {
            obj->hits[index - 1] = obj->hits[index];
        }
        obj->count -= 1;
    }
    return obj->count;
}

void hitCounterFree(HitCounter* obj) {
    free(obj->hits);
    free(obj);
}
