// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

#include <algorithm>
#include <unordered_map>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    int subtreeSum(TreeNode* node, std::unordered_map<int, int>& counts) {
        if (node == nullptr) {
            return 0;
        }
        const int total = node->val + subtreeSum(node->left, counts) + subtreeSum(node->right, counts);
        ++counts[total];
        return total;
    }

public:
    std::vector<int> findFrequentTreeSum(TreeNode* root) {
        std::unordered_map<int, int> counts;
        subtreeSum(root, counts);
        if (counts.empty()) {
            return {};
        }
        int best = 0;
        for (const auto& entry : counts) {
            best = std::max(best, entry.second);
        }
        std::vector<int> result;
        for (const auto& entry : counts) {
            if (entry.second == best) {
                result.push_back(entry.first);
            }
        }
        std::sort(result.begin(), result.end());
        return result;
    }
};
