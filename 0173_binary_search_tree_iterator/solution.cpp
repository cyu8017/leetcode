// LeetCode 0173 - Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/

#include <stack>

class BSTIterator {
    std::stack<TreeNode*> nodes;

    void pushLeft(TreeNode* node) {
        while (node) {
            nodes.push(node);
            node = node->left;
        }
    }

public:
    BSTIterator(TreeNode* root) {
        pushLeft(root);
    }

    int next() {
        TreeNode* node = nodes.top();
        nodes.pop();
        pushLeft(node->right);
        return node->val;
    }

    bool hasNext() {
        return !nodes.empty();
    }
};