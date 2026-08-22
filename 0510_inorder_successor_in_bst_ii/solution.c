// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

struct Node {
    int val;
    struct Node* left;
    struct Node* right;
    struct Node* parent;
};

struct Node* inorderSuccessor(struct Node* node) {
    if (node->right) {
        struct Node* current = node->right;
        while (current->left) {
            current = current->left;
        }
        return current;
    }

    struct Node* current = node;
    while (current->parent && current == current->parent->right) {
        current = current->parent;
    }
    return current->parent;
}
