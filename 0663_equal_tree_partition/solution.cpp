// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

#include <unordered_set>
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
    std::vector<int> subtreeSums_;

    int dfs(TreeNode* node) {
        if (!node) {
            return 0;
        }
        const int total = node->val + dfs(node->left) + dfs(node->right);
        subtreeSums_.push_back(total);
        return total;
    }

public:
    bool checkEqualTree(TreeNode* root) {
        subtreeSums_.clear();
        const int total = dfs(root);
        if (!subtreeSums_.empty()) {
            subtreeSums_.pop_back();
        }
        if (total % 2 != 0) {
            return false;
        }
        const int half = total / 2;
        for (int sum : subtreeSums_) {
            if (sum == half) {
                return true;
            }
        }
        return false;
    }
};
