// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/
// JS-only problem; C cannot express promises. Stand-in returns NULL.

typedef void* (*CallbackFn)(void** args, int argsSize);
typedef void* (*PromisifiedFn)(void** args, int argsSize);

static void* promisified_null(void** args, int argsSize) {
    (void)args; (void)argsSize;
    return NULL;
}

PromisifiedFn promisify(CallbackFn fn) {
    (void)fn;
    return promisified_null;
}
