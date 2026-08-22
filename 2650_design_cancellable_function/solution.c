// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

#include <stdlib.h>
#include <stdbool.h>

/* JS async cancellable; C port mirrors Go stub semantics. */
typedef struct {
    bool cancelled;
    bool done;
    void* result;
} Cancellable;

typedef void* (*CancellableGenerator)(void* ctx);

Cancellable* cancellableCreate(void) {
    Cancellable* c = (Cancellable*)calloc(1, sizeof(Cancellable));
    return c;
}

void cancellableCancel(Cancellable* c) {
    if (c) c->cancelled = true;
}

void* cancellableRun(Cancellable* c, CancellableGenerator gen, void* ctx, bool* ok) {
    if (!c) { if (ok) *ok = false; return NULL; }
    if (c->done) {
        if (ok) *ok = !c->cancelled;
        return c->result;
    }
    c->result = gen ? gen(ctx) : NULL;
    c->done = true;
    if (ok) *ok = !c->cancelled;
    return c->result;
}

void cancellableFree(Cancellable* c) {
    free(c);
}
