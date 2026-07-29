// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

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
    int answer_ = 0;

    std::vector<int> dfs(TreeNode* node, int distance) {
        if (!node) {
            return {};
        }
        if (!node->left && !node->right) {
            return {1};
        }
        std::vector<int> left = dfs(node->left, distance);
        std::vector<int> right = dfs(node->right, distance);
        for (int a : left) {
            for (int b : right) {
                if (a + b <= distance) {
                    answer_ += 1;
                }
            }
        }
        std::vector<int> depths;
        for (int depth : left) {
            if (depth + 1 < distance) {
                depths.push_back(depth + 1);
            }
        }
        for (int depth : right) {
            if (depth + 1 < distance) {
                depths.push_back(depth + 1);
            }
        }
        return depths;
    }

public:
    int countPairs(TreeNode* root, int distance) {
        answer_ = 0;
        dfs(root, distance);
        return answer_;
    }
};
