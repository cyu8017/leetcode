// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

#include <stdbool.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static bool is_leaf(struct TreeNode* node) {
    return node != NULL && node->left == NULL && node->right == NULL;
}

static void push_back(int** values, int* size, int* capacity, int value) {
    if (*size >= *capacity) {
        *capacity = (*capacity == 0) ? 16 : (*capacity * 2);
        *values = (int*)realloc(*values, (size_t)(*capacity) * sizeof(int));
    }
    (*values)[(*size)++] = value;
}

static void left_boundary(struct TreeNode* node, int** values, int* size, int* capacity) {
    if (node == NULL || is_leaf(node)) {
        return;
    }
    push_back(values, size, capacity, node->val);
    if (node->left) {
        left_boundary(node->left, values, size, capacity);
    } else {
        left_boundary(node->right, values, size, capacity);
    }
}

static void right_boundary(struct TreeNode* node, int** values, int* size, int* capacity) {
    if (node == NULL || is_leaf(node)) {
        return;
    }
    if (node->right) {
        right_boundary(node->right, values, size, capacity);
    } else {
        right_boundary(node->left, values, size, capacity);
    }
    push_back(values, size, capacity, node->val);
}

static void collect_leaves(struct TreeNode* node, int** values, int* size, int* capacity) {
    if (node == NULL) {
        return;
    }
    if (is_leaf(node)) {
        push_back(values, size, capacity, node->val);
        return;
    }
    collect_leaves(node->left, values, size, capacity);
    collect_leaves(node->right, values, size, capacity);
}

int* boundaryOfBinaryTree(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    if (root == NULL) {
        return NULL;
    }

    int capacity = 16;
    int* result = (int*)malloc((size_t)capacity * sizeof(int));
    if (is_leaf(root)) {
        push_back(&result, returnSize, &capacity, root->val);
        return result;
    }

    push_back(&result, returnSize, &capacity, root->val);
    left_boundary(root->left, &result, returnSize, &capacity);
    collect_leaves(root, &result, returnSize, &capacity);
    right_boundary(root->right, &result, returnSize, &capacity);
    return result;
}
