// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {
    char** keys;
    char** values;
    int size;
    int cap;
} StrMap;

static void sm_put_multi(StrMap* m, const char* k, const char* v) {
    for (int i = 0; i < m->size; i++) {
        if (strcmp(m->keys[i], k) == 0) {
            size_t nl = strlen(m->values[i]) + strlen(v) + 2;
            char* nv = (char*)malloc(nl);
            sprintf(nv, "%s,%s", m->values[i], v);
            free(m->values[i]);
            m->values[i] = nv;
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

StrMap* invertObject(StrMap* obj) {
    StrMap* out = (StrMap*)calloc(1, sizeof(StrMap));
    if (!obj) return out;
    for (int i = 0; i < obj->size; i++) sm_put_multi(out, obj->values[i], obj->keys[i]);
    return out;
}

void invertObjectFree(StrMap* m) {
    if (!m) return;
    for (int i = 0; i < m->size; i++) { free(m->keys[i]); free(m->values[i]); }
    free(m->keys); free(m->values); free(m);
}
