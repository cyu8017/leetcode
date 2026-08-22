// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/
// Simplified flat string-key merge stand-in (JS object deep merge).

#include <stdlib.h>
#include <string.h>

typedef struct {
    char** keys;
    char** values;
    int size;
    int cap;
} StrMap;

static void sm_put(StrMap* m, const char* k, const char* v) {
    for (int i = 0; i < m->size; i++) {
        if (strcmp(m->keys[i], k) == 0) {
            free(m->values[i]);
            m->values[i] = strdup(v);
            return;
        }
    }
    if (m->size == m->cap) {
        m->cap = m->cap ? m->cap * 2 : 8;
        m->keys = (char**)realloc(m->keys, m->cap * sizeof(char*));
        m->values = (char**)realloc(m->values, m->cap * sizeof(char*));
    }
    m->keys[m->size] = strdup(k);
    m->values[m->size] = strdup(v);
    m->size++;
}

StrMap* deepMerge(StrMap* obj1, StrMap* obj2) {
    StrMap* out = (StrMap*)calloc(1, sizeof(StrMap));
    if (obj1) for (int i = 0; i < obj1->size; i++) sm_put(out, obj1->keys[i], obj1->values[i]);
    if (obj2) for (int i = 0; i < obj2->size; i++) sm_put(out, obj2->keys[i], obj2->values[i]);
    return out;
}

void strMapFree(StrMap* m) {
    if (!m) return;
    for (int i = 0; i < m->size; i++) { free(m->keys[i]); free(m->values[i]); }
    free(m->keys); free(m->values); free(m);
}
