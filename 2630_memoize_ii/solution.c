// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

#include <stdlib.h>

// JavaScript problem; C stand-in identity wrapper.
typedef void* (*AnyFn)(void*);

typedef struct {
    AnyFn fn;
} MemoII;

MemoII* memoizeII(AnyFn fn) {
    MemoII* m = (MemoII*)malloc(sizeof(MemoII));
    m->fn = fn;
    return m;
}

void* memoizeIICall(MemoII* m, void* args) {
    return m->fn(args);
}

void memoizeIIFree(MemoII* m) { free(m); }
