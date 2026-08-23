// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

#include <algorithm>
#include <unordered_map>
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
    std::vector<int> treeQueries(TreeNode* root, std::vector<int>& queries) {
        std::unordered_map<int, int> height, level;
        std::unordered_map<int, std::vector<int>> levelMax;
        auto dfs = [&](auto&& self, TreeNode* node, int d) -> int {
            if (!node) return -1;
            level[node->val] = d;
            int h = 1 + std::max(self(self, node->left, d + 1), self(self, node->right, d + 1));
            height[node->val] = h;
            auto& arr = levelMax[d];
            if (arr.empty()) arr = {h};
            else if (h >= arr[0]) arr = {h, arr[0]};
            else if (arr.size() == 1 || h > arr[1]) arr = {arr[0], h};
            return h;
        };
        dfs(dfs, root, 0);
        std::vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int q = queries[i];
            int d = level[q], h = height[q];
            auto& top = levelMax[d];
            if (top[0] == h) {
                if (top.size() > 1) ans[i] = d + top[1];
                else ans[i] = d - 1;
            } else {
                ans[i] = d + top[0];
            }
        }
        return ans;
    }
};
