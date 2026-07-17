// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

#include <stdlib.h>

typedef struct {
    int root;
    int value;
} RootValue;

static int findRoot(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void unionRoots(int* parent, int a, int b) {
    int ra = findRoot(parent, a);
    int rb = findRoot(parent, b);
    if (ra != rb) {
        parent[rb] = ra;
    }
}

static int compareRootValue(const void* a, const void* b) {
    const RootValue* ra = (const RootValue*)a;
    const RootValue* rb = (const RootValue*)b;
    if (ra->root != rb->root) {
        return (ra->root > rb->root) - (ra->root < rb->root);
    }
    return (ra->value > rb->value) - (ra->value < rb->value);
}

int minimumHammingDistance(int* source, int sourceSize, int* target, int targetSize,
                           int** allowedSwaps, int allowedSwapsSize, int* allowedSwapsColSize) {
    int n = sourceSize;
    int* parent = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }
    for (int i = 0; i < allowedSwapsSize; i++) {
        unionRoots(parent, allowedSwaps[i][0], allowedSwaps[i][1]);
    }

    RootValue* fromSource = (RootValue*)malloc(n * sizeof(RootValue));
    RootValue* fromTarget = (RootValue*)malloc(n * sizeof(RootValue));
    for (int i = 0; i < n; i++) {
        int root = findRoot(parent, i);
        fromSource[i].root = root;
        fromSource[i].value = source[i];
        fromTarget[i].root = root;
        fromTarget[i].value = target[i];
    }
    qsort(fromSource, n, sizeof(RootValue), compareRootValue);
    qsort(fromTarget, n, sizeof(RootValue), compareRootValue);

    int matched = 0;
    int i = 0;
    int j = 0;
    while (i < n && j < n) {
        int cmp = compareRootValue(&fromSource[i], &fromTarget[j]);
        if (cmp == 0) {
            matched++;
            i++;
            j++;
        } else if (cmp < 0) {
            i++;
        } else {
            j++;
        }
    }

    free(parent);
    free(fromSource);
    free(fromTarget);
    return n - matched;
}
