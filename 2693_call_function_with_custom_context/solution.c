// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

#include <stdlib.h>

typedef void* (*CallFn)(void* ctx, void* args);

void* call(CallFn fn, void* ctx, void* args) {
    return fn ? fn(ctx, args) : NULL;
}
