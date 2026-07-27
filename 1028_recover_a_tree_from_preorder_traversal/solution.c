// LeetCode 1028 - Recover a Tree From Preorder Traversal
// https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* recoverFromPreorder(char* traversal) {
    int n = (int)strlen(traversal);
    struct TreeNode** stack = (struct TreeNode**)malloc((size_t)n * sizeof(struct TreeNode*));
    int top = 0;
    int i = 0;
    while (i < n) {
        int depth = 0;
        while (i < n && traversal[i] == '-') {
            depth++;
            i++;
        }
        int val = 0;
        while (i < n && isdigit((unsigned char)traversal[i])) {
            val = val * 10 + (traversal[i] - '0');
            i++;
        }
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = val;
        node->left = node->right = NULL;
        while (top > depth) top--;
        if (top > 0) {
            if (!stack[top - 1]->left) stack[top - 1]->left = node;
            else stack[top - 1]->right = node;
        }
        stack[top++] = node;
    }
    struct TreeNode* root = stack[0];
    free(stack);
    return root;
}
