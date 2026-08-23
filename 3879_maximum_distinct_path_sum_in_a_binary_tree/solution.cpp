// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    std::unordered_map<TreeNode*, std::vector<TreeNode*>> g;
    std::unordered_map<int, bool> vis;

    void dfs(TreeNode* node, TreeNode* p) {
        if (!node) return;
        g[node] = {p, node->left, node->right};
        dfs(node->left, node);
        dfs(node->right, node);
    }

    int dfs2(TreeNode* node) {
        if (!node || vis[node->val]) return 0;
        vis[node->val] = true;
        int res = node->val;
        int best = 0;
        for (TreeNode* nxt : g[node]) {
            best = std::max(best, dfs2(nxt));
        }
        vis[node->val] = false;
        return res + best;
    }

public:
    int maxSum(TreeNode* root) {
        g.clear();
        vis.clear();
        dfs(root, nullptr);
        int ans = INT_MIN;
        for (auto& [node, _] : g) {
            ans = std::max(ans, dfs2(node));
            vis.clear();
        }
        return ans;
    }
};
