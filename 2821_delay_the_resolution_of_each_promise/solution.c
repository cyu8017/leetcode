// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/
// JS Promise delay; C stand-in wraps function pointers without sleeping.

#include <stdlib.h>

typedef void* (*Thunk)(void);

typedef struct {
    Thunk* fns;
    int n;
    int ms;
} DelayedFns;

DelayedFns* delayAll(Thunk* functions, int functionsSize, int ms) {
    DelayedFns* d = (DelayedFns*)malloc(sizeof(DelayedFns));
    d->fns = functions;
    d->n = functionsSize;
    d->ms = ms;
    return d;
}

void* delayedCall(DelayedFns* d, int i) {
    (void)d->ms;
    return d->fns[i]();
}

void delayAllFree(DelayedFns* d) {
    free(d);
}
