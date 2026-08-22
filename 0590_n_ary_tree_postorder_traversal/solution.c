// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

#include <stdlib.h>

struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

static void dfs(struct Node* node, int* result, int* count) {
    if (node == NULL) {
        return;
    }
    for (int i = 0; i < node->numChildren; i++) {
        dfs(node->children[i], result, count);
    }
    result[(*count)++] = node->val;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* postorder(struct Node* root, int* returnSize) {
    int* result = (int*)malloc(10000 * sizeof(int));
    int count = 0;
    dfs(root, result, &count);
    *returnSize = count;
    return result;
}
