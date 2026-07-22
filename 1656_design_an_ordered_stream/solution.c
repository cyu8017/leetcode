// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char** data;
    int n;
    int ptr;
} OrderedStream;

OrderedStream* orderedStreamCreate(int n) {
    OrderedStream* obj = (OrderedStream*)malloc(sizeof(OrderedStream));
    obj->n = n;
    obj->ptr = 1;
    obj->data = (char**)calloc((size_t)n + 1, sizeof(char*));
    return obj;
}

char** orderedStreamInsert(OrderedStream* obj, int idKey, char* value, int* retSize) {
    obj->data[idKey] = value;
    int start = obj->ptr;
    while (obj->ptr <= obj->n && obj->data[obj->ptr] != NULL) obj->ptr++;
    *retSize = obj->ptr - start;
    if (*retSize == 0) return NULL;
    char** out = (char**)malloc((size_t)(*retSize) * sizeof(char*));
    for (int i = 0; i < *retSize; i++) out[i] = obj->data[start + i];
    return out;
}

void orderedStreamFree(OrderedStream* obj) {
    free(obj->data);
    free(obj);
}
