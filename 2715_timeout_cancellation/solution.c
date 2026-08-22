// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

#include <stdlib.h>
#include <stdbool.h>

typedef void* (*CancelFn)(void* args);

typedef struct {
    CancelFn fn;
    void* args;
    int t;
    bool cancelled;
    bool done;
    void* result;
} TimeoutCancel;

TimeoutCancel* cancellableCreate(CancelFn fn, void* args, int t) {
    TimeoutCancel* c = (TimeoutCancel*)calloc(1, sizeof(TimeoutCancel));
    c->fn = fn; c->args = args; c->t = t;
    return c;
}

void cancellableCancel(TimeoutCancel* c) {
    if (c) c->cancelled = true;
}

void* cancellableRun(TimeoutCancel* c) {
    if (!c || c->cancelled || c->done) return c ? c->result : NULL;
    c->result = c->fn ? c->fn(c->args) : NULL;
    c->done = true;
    return c->result;
}

void cancellableFree(TimeoutCancel* c) {
    free(c);
}
