// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

#include <algorithm>
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
    int countGreatEnoughNodes(TreeNode* root, int k) {
        int ans = 0;
        auto dfs = [&](auto&& self, TreeNode* node) -> std::vector<int> {
            if (!node) return {};
            std::vector<int> vals{node->val};
            auto L = self(self, node->left);
            auto R = self(self, node->right);
            vals.insert(vals.end(), L.begin(), L.end());
            vals.insert(vals.end(), R.begin(), R.end());
            int smaller = 0;
            for (int v : vals) if (v < node->val) smaller++;
            if (smaller >= k) ans++;
            return vals;
        };
        dfs(dfs, root);
        return ans;
    }
};
