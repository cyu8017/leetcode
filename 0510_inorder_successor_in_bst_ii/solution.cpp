// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

struct Node {
    int val;
    Node* left;
    Node* right;
    Node* parent;
    Node(int x) : val(x), left(nullptr), right(nullptr), parent(nullptr) {}
};

class Solution {
public:
    Node* inorderSuccessor(Node* node) {
        if (node->right) {
            Node* current = node->right;
            while (current->left) {
                current = current->left;
            }
            return current;
        }
        Node* current = node;
        while (current->parent && current == current->parent->right) {
            current = current->parent;
        }
        return current->parent;
    }
};
