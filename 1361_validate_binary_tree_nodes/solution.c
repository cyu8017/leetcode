// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool validateBinaryTreeNodes(int n, int* leftChild, int leftChildSize, int* rightChild, int rightChildSize) {
    (void)leftChildSize; (void)rightChildSize;
    int* indeg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) {
        if (leftChild[i] != -1) { if (++indeg[leftChild[i]] > 1) { free(indeg); return false; } }
        if (rightChild[i] != -1) { if (++indeg[rightChild[i]] > 1) { free(indeg); return false; } }
    }
    int root = -1;
    for (int i = 0; i < n; i++) if (indeg[i] == 0) {
        if (root != -1) { free(indeg); return false; }
        root = i;
    }
    if (root == -1) { free(indeg); return false; }
    bool* seen = (bool*)calloc(n, sizeof(bool));
    int* st = (int*)malloc(n * sizeof(int));
    int top = 0; st[top++] = root;
    int count = 0;
    while (top) {
        int u = st[--top];
        if (seen[u]) { free(indeg); free(seen); free(st); return false; }
        seen[u] = true; count++;
        if (leftChild[u] != -1) st[top++] = leftChild[u];
        if (rightChild[u] != -1) st[top++] = rightChild[u];
    }
    free(indeg); free(seen); free(st);
    return count == n;
}
