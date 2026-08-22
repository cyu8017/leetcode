// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

#include <stdlib.h>
#include <stdbool.h>

typedef void (*ThrottleFn)(void* args);

typedef struct {
    ThrottleFn fn;
    int t;
    long long last;
} Throttle;

Throttle* throttleCreate(ThrottleFn fn, int t) {
    Throttle* th = (Throttle*)malloc(sizeof(Throttle));
    th->fn = fn;
    th->t = t;
    th->last = -1000000000000LL;
    return th;
}

void throttleCall(Throttle* th, void* args, long long nowMs) {
    if (!th) return;
    if (nowMs - th->last >= th->t) {
        th->last = nowMs;
        if (th->fn) th->fn(args);
    }
}

void throttleFree(Throttle* th) {
    free(th);
}
