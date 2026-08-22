// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    void* val;
} Expect;

Expect* expectCreate(void* val) {
    Expect* e = (Expect*)malloc(sizeof(Expect));
    e->val = val;
    return e;
}

bool expectToBe(Expect* e, void* other) {
    return e->val == other;
}

bool expectNotToBe(Expect* e, void* other) {
    return e->val != other;
}

void expectFree(Expect* e) {
    free(e);
}
