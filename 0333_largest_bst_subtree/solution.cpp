// LeetCode 0333 - Largest BST Subtree
// https://leetcode.com/problems/largest-bst-subtree/

#include <algorithm>
#include <climits>
#include <tuple>
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
    int largestBSTSubtree(TreeNode* root) {
        int best = 0;
        dfs(root, best);
        return best;
    }

private:
    std::tuple<bool, int, int, int> dfs(TreeNode* node, int& best) {
        if (node == nullptr) {
            return {true, INT_MAX, INT_MIN, 0};
        }

        auto [leftOk, leftMin, leftMax, leftSize] = dfs(node->left, best);
        auto [rightOk, rightMin, rightMax, rightSize] = dfs(node->right, best);

        if (leftOk && rightOk && leftMax < node->val && node->val < rightMin) {
            int size = leftSize + rightSize + 1;
            best = std::max(best, size);
            return {true, std::min(leftMin, node->val), std::max(rightMax, node->val), size};
        }

        return {false, 0, 0, 0};
    }
};
