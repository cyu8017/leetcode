// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

#include <stack>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void recoverTree(TreeNode* root) {
        TreeNode* first = nullptr;
        TreeNode* second = nullptr;
        TreeNode* previous = nullptr;
        std::stack<TreeNode*> stack;
        TreeNode* current = root;

        while (current || !stack.empty()) {
            while (current) {
                stack.push(current);
                current = current->left;
            }
            current = stack.top();
            stack.pop();
            if (previous && previous->val > current->val) {
                if (!first) {
                    first = previous;
                }
                second = current;
            }
            previous = current;
            current = current->right;
        }

        if (first && second) {
            int temp = first->val;
            first->val = second->val;
            second->val = temp;
        }
    }
};
