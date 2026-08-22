// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

#include <stdlib.h>

typedef int (*IntUnary)(int);

typedef struct {
    IntUnary* functions;
    int size;
} Composed;

Composed* compose(IntUnary* functions, int functionsSize) {
    Composed* c = (Composed*)malloc(sizeof(Composed));
    c->functions = functions;
    c->size = functionsSize;
    return c;
}

int composedCall(Composed* c, int x) {
    for (int i = c->size - 1; i >= 0; i--) x = c->functions[i](x);
    return x;
}

void composedFree(Composed* c) { free(c); }
