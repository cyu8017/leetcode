// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>

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
    int amountOfTime(TreeNode* root, int start) {
        std::unordered_map<int, std::vector<int>> g;
        auto build = [&](auto&& self, TreeNode* node, TreeNode* parent) -> void {
            if (!node) return;
            if (parent) {
                g[node->val].push_back(parent->val);
                g[parent->val].push_back(node->val);
            }
            self(self, node->left, node);
            self(self, node->right, node);
        };
        build(build, root, nullptr);
        int ans = 0;
        std::unordered_set<int> vis{start};
        std::queue<std::pair<int, int>> q;
        q.push({start, 0});
        while (!q.empty()) {
            auto [v, d] = q.front();
            q.pop();
            ans = std::max(ans, d);
            for (int nxt : g[v]) {
                if (!vis.count(nxt)) {
                    vis.insert(nxt);
                    q.push({nxt, d + 1});
                }
            }
        }
        return ans;
    }
};
