// LeetCode 1483 - Kth Ancestor of a Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

#include <stdlib.h>

typedef struct {
    int** up;
    int width;
    int n;
} TreeAncestor;

TreeAncestor* treeAncestorCreate(int n, int* parent, int parentSize) {
    (void)parentSize;
    TreeAncestor* obj = (TreeAncestor*)malloc(sizeof(TreeAncestor));
    obj->n = n;
    obj->width = 1;
    while ((1 << obj->width) <= n) obj->width++;
    obj->up = (int**)malloc(obj->width * sizeof(int*));
    obj->up[0] = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) obj->up[0][i] = parent[i];
    for (int bit = 1; bit < obj->width; bit++) {
        obj->up[bit] = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) {
            int p = obj->up[bit - 1][i];
            obj->up[bit][i] = p == -1 ? -1 : obj->up[bit - 1][p];
        }
    }
    return obj;
}

int treeAncestorGetKthAncestor(TreeAncestor* obj, int node, int k) {
    int bit = 0;
    while (k && node != -1) {
        if (k & 1) {
            if (bit >= obj->width) return -1;
            node = obj->up[bit][node];
        }
        bit++;
        k >>= 1;
    }
    return node;
}

void treeAncestorFree(TreeAncestor* obj) {
    for (int i = 0; i < obj->width; i++) free(obj->up[i]);
    free(obj->up); free(obj);
}
