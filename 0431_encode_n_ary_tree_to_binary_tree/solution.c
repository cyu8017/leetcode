// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

#include <stdlib.h>

struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* encode(struct Node* root) {
    if (root == NULL) {
        return NULL;
    }
    struct TreeNode* binary = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    binary->val = root->val;
    binary->left = NULL;
    binary->right = NULL;
    if (root->numChildren == 0) {
        return binary;
    }
    binary->left = encode(root->children[0]);
    struct TreeNode* sibling = binary->left;
    for (int i = 1; i < root->numChildren; i++) {
        sibling->right = encode(root->children[i]);
        sibling = sibling->right;
    }
    return binary;
}

struct Node* decode(struct TreeNode* root) {
    if (root == NULL) {
        return NULL;
    }
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->val = root->val;
    node->numChildren = 0;
    node->children = NULL;

    int capacity = 0;
    struct TreeNode* current = root->left;
    while (current) {
        if (node->numChildren == capacity) {
            capacity = capacity == 0 ? 4 : capacity * 2;
            node->children = (struct Node**)realloc(node->children, (size_t)capacity * sizeof(struct Node*));
        }
        node->children[node->numChildren++] = decode(current);
        current = current->right;
    }
    return node;
}
