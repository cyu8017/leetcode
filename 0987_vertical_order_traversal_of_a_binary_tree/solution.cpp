// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

#include <algorithm>
#include <map>
#include <tuple>
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
    std::vector<std::vector<int>> verticalTraversal(TreeNode* root) {
        std::vector<std::tuple<int, int, int>> nodes;
        auto dfs = [&](auto&& self, TreeNode* node, int row, int col) -> void {
            if (!node) return;
            nodes.emplace_back(col, row, node->val);
            self(self, node->left, row + 1, col - 1);
            self(self, node->right, row + 1, col + 1);
        };
        dfs(dfs, root, 0, 0);
        std::sort(nodes.begin(), nodes.end());
        std::map<int, std::vector<int>> byCol;
        for (auto& [col, row, val] : nodes) byCol[col].push_back(val);
        std::vector<std::vector<int>> ans;
        for (auto& [_, vals] : byCol) ans.push_back(vals);
        return ans;
    }
};
