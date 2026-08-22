// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

#include <stdlib.h>
#include <stdbool.h>

typedef int (*TimedFn)(int* err);

typedef struct {
    TimedFn fn;
    int t;
} Limited;

Limited* timeLimit(TimedFn fn, int t) {
    Limited* L = (Limited*)malloc(sizeof(Limited));
    L->fn = fn;
    L->t = t;
    return L;
}

// Stand-in: invoke immediately (no async timeout available in pure C LeetCode style).
int limitedCall(Limited* L, int* err) {
    (void)L->t;
    return L->fn(err);
}

void limitedFree(Limited* L) { free(L); }
