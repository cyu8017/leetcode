// LeetCode 0314 - Binary Tree Vertical Order Traversal
// https://leetcode.com/problems/binary-tree-vertical-order-traversal/

#include <deque>
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
public:
    std::vector<std::vector<int>> verticalOrder(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }

        std::unordered_map<int, std::vector<int>> columns;
        std::deque<std::pair<TreeNode*, int>> queue;
        queue.push_back({root, 0});
        int minCol = 0;
        int maxCol = 0;

        while (!queue.empty()) {
            auto [node, column] = queue.front();
            queue.pop_front();
            minCol = std::min(minCol, column);
            maxCol = std::max(maxCol, column);
            columns[column].push_back(node->val);
            if (node->left != nullptr) {
                queue.push_back({node->left, column - 1});
            }
            if (node->right != nullptr) {
                queue.push_back({node->right, column + 1});
            }
        }

        std::vector<std::vector<int>> result;
        for (int column = minCol; column <= maxCol; column++) {
            result.push_back(columns[column]);
        }
        return result;
    }
};
