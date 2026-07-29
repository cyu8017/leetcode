// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

#include <stdlib.h>

typedef struct {
    int* encoding;
    int encodingSize;
    int i;
} RLEIterator;

RLEIterator* rLEIteratorCreate(int* encoding, int encodingSize) {
    RLEIterator* obj = (RLEIterator*)malloc(sizeof(RLEIterator));
    obj->encoding = encoding;
    obj->encodingSize = encodingSize;
    obj->i = 0;
    return obj;
}

int rLEIteratorNext(RLEIterator* obj, int n) {
    while (obj->i < obj->encodingSize) {
        if (obj->encoding[obj->i] >= n) {
            obj->encoding[obj->i] -= n;
            return obj->encoding[obj->i + 1];
        }
        n -= obj->encoding[obj->i];
        obj->i += 2;
    }
    return -1;
}

void rLEIteratorFree(RLEIterator* obj) {
    free(obj);
}
