// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

#include <cmath>
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
    std::vector<int> closestKValues(TreeNode* root, double target, int k) {
        std::vector<int> values;
        inorder(root, values);

        int lo = 0;
        int hi = static_cast<int>(values.size());
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (values[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        int left = lo - 1;
        int right = lo;
        std::vector<int> result;
        while (static_cast<int>(result.size()) < k) {
            if (right >= static_cast<int>(values.size()) ||
                (left >= 0 && std::abs(values[left] - target) <= std::abs(values[right] - target))) {
                result.push_back(values[left]);
                left--;
            } else {
                result.push_back(values[right]);
                right++;
            }
        }
        return result;
    }

private:
    void inorder(TreeNode* node, std::vector<int>& values) {
        if (!node) {
            return;
        }
        inorder(node->left, values);
        values.push_back(node->val);
        inorder(node->right, values);
    }
};
