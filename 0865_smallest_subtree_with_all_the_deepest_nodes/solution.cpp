// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

#include <utility>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        auto dfs = [](auto&& self, TreeNode* node) -> std::pair<int, TreeNode*> {
            if (!node) {
                return {0, nullptr};
            }
            auto [ld, ln] = self(self, node->left);
            auto [rd, rn] = self(self, node->right);
            if (ld > rd) {
                return {ld + 1, ln};
            }
            if (rd > ld) {
                return {rd + 1, rn};
            }
            return {ld + 1, node};
        };
        return dfs(dfs, root).second;
    }
};
