// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* values;
    int size;
    int index;
    int peeked;
    bool hasPeeked;
} PeekingIterator;

PeekingIterator* peekingIteratorCreate(int* arr, int arrSize) {
    PeekingIterator* obj = (PeekingIterator*)malloc(sizeof(PeekingIterator));
    obj->values = arr;
    obj->size = arrSize;
    obj->index = 0;
    obj->hasPeeked = false;
    return obj;
}

int peekingIteratorPeek(PeekingIterator* obj) {
    if (!obj->hasPeeked) {
        obj->peeked = obj->values[obj->index++];
        obj->hasPeeked = true;
    }
    return obj->peeked;
}

int peekingIteratorNext(PeekingIterator* obj) {
    if (obj->hasPeeked) {
        obj->hasPeeked = false;
        return obj->peeked;
    }
    return obj->values[obj->index++];
}

bool peekingIteratorHasNext(PeekingIterator* obj) {
    return obj->hasPeeked || obj->index < obj->size;
}

void peekingIteratorFree(PeekingIterator* obj) {
    free(obj);
}
