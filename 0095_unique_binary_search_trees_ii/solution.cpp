// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

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
    std::vector<TreeNode*> generateTrees(int n) {
        if (n == 0) {
            return {};
        }
        return build(1, n);
    }

private:
    std::vector<TreeNode*> build(int start, int end) {
        if (start > end) {
            return {nullptr};
        }
        std::vector<TreeNode*> trees;
        for (int rootVal = start; rootVal <= end; ++rootVal) {
            std::vector<TreeNode*> leftTrees = build(start, rootVal - 1);
            std::vector<TreeNode*> rightTrees = build(rootVal + 1, end);
            for (TreeNode* left : leftTrees) {
                for (TreeNode* right : rightTrees) {
                    trees.push_back(new TreeNode(rootVal, left, right));
                }
            }
        }
        return trees;
    }
};
