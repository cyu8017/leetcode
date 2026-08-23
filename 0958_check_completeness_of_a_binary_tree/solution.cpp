// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

#include <queue>

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
    bool isCompleteTree(TreeNode* root) {
        std::queue<TreeNode*> q;
        q.push(root);
        bool end = false;
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            if (!node) {
                end = true;
            } else {
                if (end) return false;
                q.push(node->left);
                q.push(node->right);
            }
        }
        return true;
    }
};
