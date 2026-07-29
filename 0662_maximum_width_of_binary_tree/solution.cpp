// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

#include <algorithm>
#include <queue>
#include <utility>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        if (!root) {
            return 0;
        }
        std::queue<std::pair<TreeNode*, unsigned long long>> queue;
        queue.emplace(root, 0);
        int best = 0;
        while (!queue.empty()) {
            const unsigned long long left = queue.front().second;
            const int size = static_cast<int>(queue.size());
            for (int i = 0; i < size; ++i) {
                auto [node, idx] = queue.front();
                queue.pop();
                best = std::max(best, static_cast<int>(idx - left + 1));
                if (node->left) {
                    queue.emplace(node->left, idx * 2);
                }
                if (node->right) {
                    queue.emplace(node->right, idx * 2 + 1);
                }
            }
        }
        return best;
    }
};
