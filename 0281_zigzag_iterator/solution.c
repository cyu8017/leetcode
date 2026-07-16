// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int** vectors;
    int* vectorSizes;
    int vectorCount;
    int* indices;
    int turn;
} ZigzagIterator;

ZigzagIterator* zigzagIteratorCreate(int* v1, int v1Size, int* v2, int v2Size) {
    ZigzagIterator* obj = (ZigzagIterator*)malloc(sizeof(ZigzagIterator));
    obj->vectorCount = 2;
    obj->vectors = (int**)malloc(2 * sizeof(int*));
    obj->vectorSizes = (int*)malloc(2 * sizeof(int));
    obj->indices = (int*)calloc(2, sizeof(int));
    obj->vectors[0] = v1;
    obj->vectors[1] = v2;
    obj->vectorSizes[0] = v1Size;
    obj->vectorSizes[1] = v2Size;
    obj->turn = 0;
    return obj;
}

int zigzagIteratorNext(ZigzagIterator* obj) {
    while (obj->indices[obj->turn] >= obj->vectorSizes[obj->turn]) {
        obj->turn = 1 - obj->turn;
    }
    int value = obj->vectors[obj->turn][obj->indices[obj->turn]];
    obj->indices[obj->turn] += 1;
    obj->turn = 1 - obj->turn;
    return value;
}

bool zigzagIteratorHasNext(ZigzagIterator* obj) {
    for (int index = 0; index < obj->vectorCount; index++) {
        if (obj->indices[index] < obj->vectorSizes[index]) {
            return true;
        }
    }
    return false;
}

void zigzagIteratorFree(ZigzagIterator* obj) {
    free(obj->vectors);
    free(obj->vectorSizes);
    free(obj->indices);
    free(obj);
}
