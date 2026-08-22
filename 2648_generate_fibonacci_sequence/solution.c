// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

#include <stdlib.h>

typedef struct {
    int a, b;
} FibGenerator;

FibGenerator* fibGeneratorCreate(void) {
    FibGenerator* g = (FibGenerator*)malloc(sizeof(FibGenerator));
    g->a = 0;
    g->b = 1;
    return g;
}

int fibGeneratorNext(FibGenerator* g) {
    int v = g->a;
    int na = g->b;
    g->b = g->a + g->b;
    g->a = na;
    return v;
}

void fibGeneratorFree(FibGenerator* g) {
    free(g);
}
