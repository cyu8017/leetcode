// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

#include <stdlib.h>
#include <stdbool.h>

typedef void* (*OnceFn)(void* args);

typedef struct {
    OnceFn fn;
    bool called;
    void* res;
} OnceWrapper;

OnceWrapper* onceCreate(OnceFn fn) {
    OnceWrapper* w = (OnceWrapper*)calloc(1, sizeof(OnceWrapper));
    w->fn = fn;
    return w;
}

void* onceCall(OnceWrapper* w, void* args) {
    if (!w || w->called) return NULL;
    w->called = true;
    w->res = w->fn ? w->fn(args) : NULL;
    return w->res;
}

void onceFree(OnceWrapper* w) {
    free(w);
}
