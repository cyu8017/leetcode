// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

#include <stdlib.h>

typedef void* (*AsyncFn)(void);

void** promiseAll(AsyncFn* functions, int functionsSize, int* returnSize) {
    void** ans = (void**)malloc((size_t)functionsSize * sizeof(void*));
    for (int i = 0; i < functionsSize; i++)
        ans[i] = functions[i] ? functions[i]() : NULL;
    *returnSize = functionsSize;
    return ans;
}
