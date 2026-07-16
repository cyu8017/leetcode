// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

#include <vector>

class Node {
public:
    int val;
    std::vector<Node*> children;
    Node() : val(0) {}
    explicit Node(int _val) : val(_val) {}
    Node(int _val, std::vector<Node*> _children) : val(_val), children(std::move(_children)) {}
};

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* encodeNaryTree(Node* root) {
        if (root == nullptr) {
            return nullptr;
        }

        TreeNode* binary = new TreeNode(root->val);
        if (root->children.empty()) {
            return binary;
        }

        binary->left = encodeNaryTree(root->children[0]);
        TreeNode* sibling = binary->left;
        for (size_t index = 1; index < root->children.size(); ++index) {
            sibling->right = encodeNaryTree(root->children[index]);
            sibling = sibling->right;
        }
        return binary;
    }

    Node* decodeBinaryTree(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        Node* node = new Node(root->val);
        TreeNode* current = root->left;
        while (current != nullptr) {
            node->children.push_back(decodeBinaryTree(current));
            current = current->right;
        }
        return node;
    }
};
