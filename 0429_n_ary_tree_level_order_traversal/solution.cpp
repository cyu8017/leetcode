// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

#include <queue>
#include <vector>

class Node {
public:
    int val;
    std::vector<Node*> children;
    Node() : val(0) {}
    explicit Node(int _val) : val(_val) {}
    Node(int _val, std::vector<Node*> _children) : val(_val), children(std::move(_children)) {}
};

class Solution {
public:
    std::vector<std::vector<int>> levelOrder(Node* root) {
        std::vector<std::vector<int>> result;
        if (root == nullptr) {
            return result;
        }

        std::queue<Node*> queue;
        queue.push(root);

        while (!queue.empty()) {
            int size = static_cast<int>(queue.size());
            std::vector<int> level;
            level.reserve(size);
            for (int index = 0; index < size; ++index) {
                Node* node = queue.front();
                queue.pop();
                level.push_back(node->val);
                for (Node* child : node->children) {
                    queue.push(child);
                }
            }
            result.push_back(std::move(level));
        }

        return result;
    }
};
