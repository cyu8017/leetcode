// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

#include <stdlib.h>

typedef int (*IntVarFn)(int* args, int n);

typedef struct {
    IntVarFn fn;
    int* fixed;
    int* isPlaceholder; // 1 if placeholder
    int fixedSize;
} PartialFn;

PartialFn* partialCreate(IntVarFn fn, int* args, int* isPlaceholder, int argsSize) {
    PartialFn* p = (PartialFn*)malloc(sizeof(PartialFn));
    p->fn = fn;
    p->fixedSize = argsSize;
    p->fixed = (int*)malloc(argsSize * sizeof(int));
    p->isPlaceholder = (int*)malloc(argsSize * sizeof(int));
    for (int i = 0; i < argsSize; i++) {
        p->fixed[i] = args[i];
        p->isPlaceholder[i] = isPlaceholder[i];
    }
    return p;
}

int partialCall(PartialFn* p, int* rest, int restSize) {
    int* full = (int*)malloc((p->fixedSize + restSize) * sizeof(int));
    int fi = 0, ri = 0;
    for (int i = 0; i < p->fixedSize; i++) {
        if (p->isPlaceholder[i]) {
            if (ri < restSize) full[fi++] = rest[ri++];
        } else full[fi++] = p->fixed[i];
    }
    while (ri < restSize) full[fi++] = rest[ri++];
    int ans = p->fn(full, fi);
    free(full);
    return ans;
}

void partialFree(PartialFn* p) {
    if (!p) return;
    free(p->fixed);
    free(p->isPlaceholder);
    free(p);
}
