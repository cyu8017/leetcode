// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

#include <stdlib.h>

typedef struct {
    int cur;
} Counter;

Counter* createCounter(int n) {
    Counter* c = (Counter*)malloc(sizeof(Counter));
    c->cur = n;
    return c;
}

int counterNext(Counter* c) {
    return c->cur++;
}

void counterFree(Counter* c) {
    free(c);
}
