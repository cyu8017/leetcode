// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

#include <stdbool.h>
#include <stdlib.h>

bool isPreorder(int** nodes, int nodesSize, int* nodesColSize) {
    (void)nodesColSize;
    if (nodesSize == 0) return true;
    int* stack = (int*)malloc(nodesSize * sizeof(int));
    int top = 0;
    stack[top++] = nodes[0][0];
    for (int i = 1; i < nodesSize; i++) {
        int id = nodes[i][0], parent = nodes[i][1];
        while (top > 0 && stack[top - 1] != parent) top--;
        if (top == 0) { free(stack); return false; }
        stack[top++] = id;
    }
    free(stack);
    return true;
}
