// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

#include <algorithm>
#include <unordered_map>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    void inorder(TreeNode* node, std::unordered_map<int, int>& counts, int& best) {
        if (node == nullptr) {
            return;
        }
        inorder(node->left, counts, best);
        const int count = ++counts[node->val];
        best = std::max(best, count);
        inorder(node->right, counts, best);
    }

public:
    std::vector<int> findMode(TreeNode* root) {
        std::unordered_map<int, int> counts;
        int best = 0;
        inorder(root, counts, best);
        std::vector<int> result;
        for (const auto& entry : counts) {
            if (entry.second == best) {
                result.push_back(entry.first);
            }
        }
        return result;
    }
};
