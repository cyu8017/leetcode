// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

#include <stdlib.h>
#include <stdbool.h>

typedef void (*IntervalFn)(void* args);

typedef struct {
    IntervalFn fn;
    void* args;
    int t;
    bool cancelled;
} IntervalCancel;

IntervalCancel* intervalCancellableCreate(IntervalFn fn, void* args, int t) {
    IntervalCancel* c = (IntervalCancel*)calloc(1, sizeof(IntervalCancel));
    c->fn = fn; c->args = args; c->t = t;
    if (c->fn) c->fn(c->args);
    return c;
}

void intervalCancellableCancel(IntervalCancel* c) {
    if (c) c->cancelled = true;
}

void intervalCancellableTick(IntervalCancel* c) {
    if (c && !c->cancelled && c->fn) c->fn(c->args);
}

void intervalCancellableFree(IntervalCancel* c) {
    free(c);
}
