// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

#include <algorithm>
#include <string>
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
    int height(TreeNode* node) {
        if (!node) {
            return -1;
        }
        return 1 + std::max(height(node->left), height(node->right));
    }

    void place(TreeNode* node, int r, int c, int h, std::vector<std::vector<std::string>>& res) {
        if (!node) {
            return;
        }
        res[r][c] = std::to_string(node->val);
        if (r == h) {
            return;
        }
        const int offset = 1 << (h - r - 1);
        place(node->left, r + 1, c - offset, h, res);
        place(node->right, r + 1, c + offset, h, res);
    }

public:
    std::vector<std::vector<std::string>> printTree(TreeNode* root) {
        const int h = height(root);
        const int rows = h + 1;
        const int cols = (1 << (h + 1)) - 1;
        std::vector<std::vector<std::string>> res(rows, std::vector<std::string>(cols, ""));
        place(root, 0, (cols - 1) / 2, h, res);
        return res;
    }
};
