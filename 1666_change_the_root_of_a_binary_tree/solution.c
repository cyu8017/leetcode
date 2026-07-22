// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

#include <stddef.h>

struct Node {
    int val;
    struct Node* left;
    struct Node* right;
    struct Node* parent;
};

static void fixParent(struct Node* cur, struct Node* parent) {
    if (!cur) return;
    cur->parent = parent;
    fixParent(cur->left, cur);
    fixParent(cur->right, cur);
}

struct Node* flipBinaryTree(struct Node* root, struct Node* leaf) {
    struct Node* node = leaf;
    while (node != root) {
        struct Node* parent = node->parent;
        if (parent->left == node) parent->left = NULL;
        else parent->right = NULL;
        struct Node* originalLeft = node->left;
        node->left = parent;
        if (originalLeft) node->right = originalLeft;
        node = parent;
    }
    fixParent(leaf, NULL);
    return leaf;
}
