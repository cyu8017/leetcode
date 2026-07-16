// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    static bool isLeaf(TreeNode* node) {
        return node && !node->left && !node->right;
    }

    void leftBoundary(TreeNode* node, std::vector<int>& result) {
        if (!node || isLeaf(node)) {
            return;
        }
        result.push_back(node->val);
        if (node->left) {
            leftBoundary(node->left, result);
        } else {
            leftBoundary(node->right, result);
        }
    }

    void rightBoundary(TreeNode* node, std::vector<int>& result) {
        if (!node || isLeaf(node)) {
            return;
        }
        if (node->right) {
            rightBoundary(node->right, result);
        } else {
            rightBoundary(node->left, result);
        }
        result.push_back(node->val);
    }

    void collectLeaves(TreeNode* node, std::vector<int>& result) {
        if (!node) {
            return;
        }
        if (isLeaf(node)) {
            result.push_back(node->val);
            return;
        }
        collectLeaves(node->left, result);
        collectLeaves(node->right, result);
    }

public:
    std::vector<int> boundaryOfBinaryTree(TreeNode* root) {
        if (!root) {
            return {};
        }
        if (isLeaf(root)) {
            return {root->val};
        }

        std::vector<int> result = {root->val};
        leftBoundary(root->left, result);
        collectLeaves(root, result);
        rightBoundary(root->right, result);
        return result;
    }
};
