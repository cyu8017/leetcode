// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

#include <stddef.h>

struct Node {
    int val;
    struct Node* left;
    struct Node* right;
};

static void inorder(struct Node* node, struct Node** first, struct Node** last) {
    if (node == NULL) {
        return;
    }
    inorder(node->left, first, last);
    if (*last) {
        (*last)->right = node;
        node->left = *last;
    } else {
        *first = node;
    }
    *last = node;
    inorder(node->right, first, last);
}

struct Node* treeToDoublyList(struct Node* root) {
    if (root == NULL) {
        return NULL;
    }
    struct Node* first = NULL;
    struct Node* last = NULL;
    inorder(root, &first, &last);
    if (first && last) {
        first->left = last;
        last->right = first;
    }
    return first;
}
