// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

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
    int countUnivalSubtrees(TreeNode* root) {
        int count = 0;
        dfs(root, count);
        return count;
    }

private:
    bool dfs(TreeNode* node, int& count) {
        if (!node) {
            return true;
        }
        bool leftOk = dfs(node->left, count);
        bool rightOk = dfs(node->right, count);
        if (!leftOk || !rightOk) {
            return false;
        }
        if (node->left && node->left->val != node->val) {
            return false;
        }
        if (node->right && node->right->val != node->val) {
            return false;
        }
        count++;
        return true;
    }
};
