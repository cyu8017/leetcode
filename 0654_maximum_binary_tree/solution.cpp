// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

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
    std::vector<int>* nums_ = nullptr;

    TreeNode* build(int left, int right) {
        if (left > right) {
            return nullptr;
        }
        int mid = left;
        for (int i = left; i <= right; ++i) {
            if ((*nums_)[i] > (*nums_)[mid]) {
                mid = i;
            }
        }
        return new TreeNode((*nums_)[mid], build(left, mid - 1), build(mid + 1, right));
    }

public:
    TreeNode* constructMaximumBinaryTree(std::vector<int>& nums) {
        nums_ = &nums;
        return build(0, static_cast<int>(nums.size()) - 1);
    }
};
