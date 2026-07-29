// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int height(struct TreeNode* node) {
    if (!node) return -1;
    int l = height(node->left), r = height(node->right);
    return 1 + (l > r ? l : r);
}

static void place(struct TreeNode* node, char*** res, int h, int r, int c) {
    if (!node) return;
    char buf[16];
    snprintf(buf, sizeof(buf), "%d", node->val);
    res[r][c] = strdup(buf);
    if (r == h) return;
    int offset = 1 << (h - r - 1);
    place(node->left, res, h, r + 1, c - offset);
    place(node->right, res, h, r + 1, c + offset);
}

char*** printTree(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    int h = height(root);
    int rows = h + 1;
    int cols = (1 << (h + 1)) - 1;
    char*** res = (char***)malloc((size_t)rows * sizeof(char**));
    *returnColumnSizes = (int*)malloc((size_t)rows * sizeof(int));
    for (int i = 0; i < rows; i++) {
        res[i] = (char**)malloc((size_t)cols * sizeof(char*));
        (*returnColumnSizes)[i] = cols;
        for (int j = 0; j < cols; j++) res[i][j] = strdup("");
    }
    place(root, res, h, 0, (cols - 1) / 2);
    *returnSize = rows;
    return res;
}
