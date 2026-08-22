// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/
// Flat string-map filter stand-in for JS deep object filter.

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    char** keys;
    char** values;
    int size;
} StrMap;

typedef bool (*FilterFn)(const char* value);

StrMap* deepFilter(StrMap* obj, FilterFn fn) {
    StrMap* out = (StrMap*)calloc(1, sizeof(StrMap));
    if (!obj) return out;
    out->keys = (char**)malloc(obj->size * sizeof(char*));
    out->values = (char**)malloc(obj->size * sizeof(char*));
    for (int i = 0; i < obj->size; i++) {
        if (fn(obj->values[i])) {
            out->keys[out->size] = strdup(obj->keys[i]);
            out->values[out->size] = strdup(obj->values[i]);
            out->size++;
        }
    }
    return out;
}

void deepFilterFree(StrMap* m) {
    if (!m) return;
    for (int i = 0; i < m->size; i++) { free(m->keys[i]); free(m->values[i]); }
    free(m->keys); free(m->values); free(m);
}
