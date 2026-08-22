// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

#include <stdlib.h>

// JavaScript timing problem; C stand-in stores last args and delay metadata.
typedef void (*VoidFn)(void*);

typedef struct {
    VoidFn fn;
    int t;
    void* lastArgs;
} Debounced;

Debounced* debounce(VoidFn fn, int t) {
    Debounced* d = (Debounced*)calloc(1, sizeof(Debounced));
    d->fn = fn;
    d->t = t;
    return d;
}

void debouncedCall(Debounced* d, void* args) {
    d->lastArgs = args;
    // Without an event loop, invoke immediately (stand-in).
    if (d->fn) d->fn(args);
}

void debouncedFree(Debounced* d) { free(d); }
