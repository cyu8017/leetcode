// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

#include <stdlib.h>

typedef int (*VarFn)(int*, int);

typedef struct {
    VarFn fn;
    int arity;
    int* args;
    int size;
} Curry;

Curry* curryCreate(VarFn fn, int arity) {
    Curry* c = (Curry*)calloc(1, sizeof(Curry));
    c->fn = fn;
    c->arity = arity;
    c->args = (int*)malloc((size_t)arity * sizeof(int));
    return c;
}

int curryCall(Curry* c, int* more, int moreSize, int* done) {
    for (int i = 0; i < moreSize && c->size < c->arity; i++) c->args[c->size++] = more[i];
    if (c->size >= c->arity) {
        *done = 1;
        return c->fn(c->args, c->arity);
    }
    *done = 0;
    return 0;
}

void curryFree(Curry* c) {
    free(c->args);
    free(c);
}
