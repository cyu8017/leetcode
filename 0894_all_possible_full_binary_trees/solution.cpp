// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

#include <functional>
#include <unordered_map>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
public:
    std::vector<TreeNode*> allPossibleFBT(int n) {
        std::unordered_map<int, std::vector<TreeNode*>> memo;
        std::function<std::vector<TreeNode*>(int)> build =
            [&](int nodes) -> std::vector<TreeNode*> {
            if (memo.count(nodes)) {
                return memo[nodes];
            }
            std::vector<TreeNode*> res;
            if (nodes % 2 == 0) {
                return memo[nodes] = res;
            }
            if (nodes == 1) {
                res.push_back(new TreeNode(0));
                return memo[nodes] = res;
            }
            for (int left = 1; left < nodes; left += 2) {
                int right = nodes - 1 - left;
                for (TreeNode* L : build(left)) {
                    for (TreeNode* R : build(right)) {
                        TreeNode* root = new TreeNode(0);
                        root->left = L;
                        root->right = R;
                        res.push_back(root);
                    }
                }
            }
            return memo[nodes] = res;
        };
        return build(n);
    }
};
