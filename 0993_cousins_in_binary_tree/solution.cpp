// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

#include <unordered_map>
#include <utility>

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
    bool isCousins(TreeNode* root, int x, int y) {
        std::unordered_map<int, std::pair<int, TreeNode*>> info;
        auto dfs = [&](auto&& self, TreeNode* node, TreeNode* parent, int depth) -> void {
            if (!node) return;
            if (node->val == x || node->val == y) info[node->val] = {depth, parent};
            self(self, node->left, node, depth + 1);
            self(self, node->right, node, depth + 1);
        };
        dfs(dfs, root, nullptr, 0);
        return info[x].first == info[y].first && info[x].second != info[y].second;
    }
};
