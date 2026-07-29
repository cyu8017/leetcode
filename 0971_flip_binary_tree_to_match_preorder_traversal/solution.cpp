// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

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
    std::vector<int> flipMatchVoyage(TreeNode* root, std::vector<int>& voyage) {
        int i = 0;
        std::vector<int> ans;
        auto dfs = [&](auto&& self, TreeNode* node) -> bool {
            if (!node) return true;
            if (node->val != voyage[i]) return false;
            i++;
            if (node->left && node->left->val != voyage[i]) {
                ans.push_back(node->val);
                return self(self, node->right) && self(self, node->left);
            }
            return self(self, node->left) && self(self, node->right);
        };
        return dfs(dfs, root) ? ans : std::vector<int>{-1};
    }
};
