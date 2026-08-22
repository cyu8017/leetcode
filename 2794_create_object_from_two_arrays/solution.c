// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/
// Map stand-in using parallel string key / void* value arrays.

#include <stdlib.h>
#include <string.h>

typedef struct {
    char** keys;
    void** values;
    int size;
} ObjectMap;

ObjectMap* createObject(char** keysArr, int keysSize, void** valuesArr, int valuesSize) {
    int n = keysSize < valuesSize ? keysSize : valuesSize;
    ObjectMap* out = (ObjectMap*)malloc(sizeof(ObjectMap));
    out->keys = (char**)malloc(n * sizeof(char*));
    out->values = (void**)malloc(n * sizeof(void*));
    out->size = 0;
    for (int i = 0; i < n; i++) {
        int exists = 0;
        for (int j = 0; j < out->size; j++) {
            if (strcmp(out->keys[j], keysArr[i]) == 0) { exists = 1; break; }
        }
        if (!exists) {
            out->keys[out->size] = keysArr[i];
            out->values[out->size] = valuesArr[i];
            out->size++;
        }
    }
    return out;
}

void createObjectFree(ObjectMap* o) {
    if (!o) return;
    free(o->keys);
    free(o->values);
    free(o);
}
