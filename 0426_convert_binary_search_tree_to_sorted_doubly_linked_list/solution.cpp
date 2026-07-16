// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    TreeNode* first = nullptr;
    TreeNode* last = nullptr;

    void inorder(TreeNode* node) {
        if (node == nullptr) {
            return;
        }
        inorder(node->left);
        if (last != nullptr) {
            last->right = node;
            node->left = last;
        } else {
            first = node;
        }
        last = node;
        inorder(node->right);
    }

public:
    TreeNode* treeToDoublyList(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        first = nullptr;
        last = nullptr;
        inorder(root);

        if (first != nullptr && last != nullptr) {
            first->left = last;
            last->right = first;
        }
        return first;
    }
};
