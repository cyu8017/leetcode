// LeetCode 0113 - Path Sum II
#include <vector>
struct TreeNode { int val; TreeNode *left, *right; };
class Solution {
    void dfs(TreeNode* n, int sum, std::vector<int>& path, std::vector<std::vector<int>>& out) {
        if (!n) return; path.push_back(n->val); sum -= n->val;
        if (!n->left && !n->right && sum == 0) out.push_back(path);
        else { dfs(n->left, sum, path, out); dfs(n->right, sum, path, out); }
        path.pop_back();
    }
public: std::vector<std::vector<int>> pathSum(TreeNode* root, int targetSum) {
    std::vector<std::vector<int>> out; std::vector<int> path; dfs(root, targetSum, path, out); return out;
} };