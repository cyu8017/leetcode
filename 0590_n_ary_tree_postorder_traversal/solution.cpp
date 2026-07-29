// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

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
    std::vector<int> postorder(Node* root) {
        std::vector<int> result;
        dfs(root, result);
        return result;
    }

private:
    void dfs(Node* node, std::vector<int>& result) {
        if (node == nullptr) {
            return;
        }
        for (Node* child : node->children) {
            dfs(child, result);
        }
        result.push_back(node->val);
    }
};
