// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/
// JS Promise.allSettled stand-in: run thunks and store results.

#include <stdlib.h>

typedef void* (*Thunk)(void);

typedef struct {
    int fulfilled; // 1 fulfilled
    void* value;
} SettledResult;

SettledResult* promiseAllSettled(Thunk* functions, int functionsSize, int* returnSize) {
    SettledResult* ans = (SettledResult*)malloc(functionsSize * sizeof(SettledResult));
    for (int i = 0; i < functionsSize; i++) {
        ans[i].fulfilled = 1;
        ans[i].value = functions[i]();
    }
    *returnSize = functionsSize;
    return ans;
}
