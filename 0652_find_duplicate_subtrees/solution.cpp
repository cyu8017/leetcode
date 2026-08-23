// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

#include <string>
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
    std::unordered_map<std::string, int> counts_;
    std::vector<TreeNode*> result_;

    std::string serialize(TreeNode* node) {
        if (!node) {
            return "#";
        }
        const std::string key =
            std::to_string(node->val) + "," + serialize(node->left) + "," +
            serialize(node->right);
        if (++counts_[key] == 2) {
            result_.push_back(node);
        }
        return key;
    }

public:
    std::vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        counts_.clear();
        result_.clear();
        serialize(root);
        return result_;
    }
};
