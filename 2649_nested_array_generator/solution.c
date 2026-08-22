// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

#include <stdlib.h>

/* Flatten nested integer arrays (inorder). LeetCode JS problem; C port of Go helper. */
typedef struct NestedInteger NestedInteger;
struct NestedInteger {
    int isInteger;
    int value;
    NestedInteger** list;
    int listSize;
};

static void dfs2649(struct NestedInteger* x, int** out, int* sz, int* cap) {
    if (!x) return;
    if (x->isInteger) {
        if (*sz == *cap) {
            *cap = *cap ? *cap * 2 : 16;
            *out = (int*)realloc(*out, (size_t)(*cap) * sizeof(int));
        }
        (*out)[(*sz)++] = x->value;
        return;
    }
    for (int i = 0; i < x->listSize; i++)
        dfs2649(x->list[i], out, sz, cap);
}

int* inorderTraversal(struct NestedInteger** arr, int arrSize, int* returnSize) {
    int* out = NULL;
    int sz = 0, cap = 0;
    for (int i = 0; i < arrSize; i++)
        dfs2649(arr[i], &out, &sz, &cap);
    *returnSize = sz;
    return out ? out : (int*)malloc(sizeof(int));
}
