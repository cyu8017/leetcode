// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

#include <queue>
#include <unordered_map>
#include <unordered_set>
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
    int findClosestLeaf(TreeNode* root, int k) {
        std::unordered_map<int, std::vector<int>> graph;
        std::unordered_set<int> leaves;
        build(root, nullptr, graph, leaves);
        std::queue<int> q;
        std::unordered_set<int> seen{k};
        q.push(k);
        while (!q.empty()) {
            int value = q.front();
            q.pop();
            if (leaves.count(value)) {
                return value;
            }
            for (int neighbor : graph[value]) {
                if (!seen.count(neighbor)) {
                    seen.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
        return -1;
    }

private:
    void build(TreeNode* node, TreeNode* parent, std::unordered_map<int, std::vector<int>>& graph,
               std::unordered_set<int>& leaves) {
        if (!node) {
            return;
        }
        if (parent) {
            graph[node->val].push_back(parent->val);
            graph[parent->val].push_back(node->val);
        }
        if (!node->left && !node->right) {
            leaves.insert(node->val);
        }
        build(node->right, node, graph, leaves);
        build(node->left, node, graph, leaves);
    }
};
