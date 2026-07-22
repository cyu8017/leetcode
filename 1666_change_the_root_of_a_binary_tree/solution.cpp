// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

#include <unordered_map>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode* parent;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr), parent(nullptr) {}
};

class Solution {
    void buildParents(TreeNode* node, TreeNode* parent, std::unordered_map<TreeNode*, TreeNode*>& parents) {
        if (!node) {
            return;
        }
        parents[node] = parent;
        buildParents(node->left, node, parents);
        buildParents(node->right, node, parents);
    }

    TreeNode* find(TreeNode* node, int val) {
        if (!node) {
            return nullptr;
        }
        if (node->val == val) {
            return node;
        }
        TreeNode* left = find(node->left, val);
        return left ? left : find(node->right, val);
    }

    void fixParent(TreeNode* cur, TreeNode* parent) {
        if (!cur) {
            return;
        }
        cur->parent = parent;
        fixParent(cur->left, cur);
        fixParent(cur->right, cur);
    }

public:
    // Harness passes leaf as int value; LeetCode API uses Node* leaf.
    TreeNode* flipBinaryTree(TreeNode* root, int leafVal) {
        std::unordered_map<TreeNode*, TreeNode*> parents;
        buildParents(root, nullptr, parents);
        TreeNode* leaf = find(root, leafVal);
        TreeNode* node = leaf;
        while (node != root) {
            TreeNode* parent = parents[node];
            if (parent->left == node) {
                parent->left = nullptr;
            } else {
                parent->right = nullptr;
            }
            TreeNode* originalLeft = node->left;
            node->left = parent;
            if (originalLeft) {
                node->right = originalLeft;
            }
            node = parent;
        }
        fixParent(leaf, nullptr);
        return leaf;
    }

    TreeNode* flipBinaryTree(TreeNode* root, TreeNode* leaf) {
        return flipBinaryTree(root, leaf->val);
    }
};
