// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

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
public:
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        std::unordered_set<int> values;
        std::vector<TreeNode*> stack;
        if (root1) {
            stack.push_back(root1);
        }
        while (!stack.empty()) {
            TreeNode* node = stack.back();
            stack.pop_back();
            values.insert(node->val);
            if (node->left) {
                stack.push_back(node->left);
            }
            if (node->right) {
                stack.push_back(node->right);
            }
        }
        if (root2) {
            stack.push_back(root2);
        }
        while (!stack.empty()) {
            TreeNode* node = stack.back();
            stack.pop_back();
            if (values.count(target - node->val)) {
                return true;
            }
            if (node->left) {
                stack.push_back(node->left);
            }
            if (node->right) {
                stack.push_back(node->right);
            }
        }
        return false;
    }
};
