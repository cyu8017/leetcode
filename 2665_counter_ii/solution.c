// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

#include <stdlib.h>

typedef struct {
    int init;
    int cur;
} CounterII;

CounterII* createCounter(int init) {
    CounterII* c = (CounterII*)malloc(sizeof(CounterII));
    c->init = init;
    c->cur = init;
    return c;
}

int counterIIIncrement(CounterII* c) {
    c->cur++;
    return c->cur;
}

int counterIIDecrement(CounterII* c) {
    c->cur--;
    return c->cur;
}

int counterIIReset(CounterII* c) {
    c->cur = c->init;
    return c->cur;
}

void counterIIFree(CounterII* c) {
    free(c);
}
