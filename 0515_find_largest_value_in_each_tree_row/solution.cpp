// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

#include <climits>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    std::vector<int> largestValues(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        std::vector<int> result;
        std::queue<TreeNode*> queue;
        queue.push(root);
        while (!queue.empty()) {
            int levelMax = INT_MIN;
            const int levelSize = static_cast<int>(queue.size());
            for (int index = 0; index < levelSize; ++index) {
                TreeNode* node = queue.front();
                queue.pop();
                levelMax = std::max(levelMax, node->val);
                if (node->left) {
                    queue.push(node->left);
                }
                if (node->right) {
                    queue.push(node->right);
                }
            }
            result.push_back(levelMax);
        }
        return result;
    }
};
