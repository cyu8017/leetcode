// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

#include <queue>
#include <vector>

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
    TreeNode* replaceValueInTree(TreeNode* root) {
        if (!root) return nullptr;
        root->val = 0;
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = (int)q.size();
            int levelSum = 0;
            std::vector<TreeNode*> level;
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node);
                if (node->left) levelSum += node->left->val;
                if (node->right) levelSum += node->right->val;
            }
            for (TreeNode* node : level) {
                int cousin = levelSum;
                if (node->left) cousin -= node->left->val;
                if (node->right) cousin -= node->right->val;
                if (node->left) {
                    node->left->val = cousin;
                    q.push(node->left);
                }
                if (node->right) {
                    node->right->val = cousin;
                    q.push(node->right);
                }
            }
        }
        return root;
    }
};
