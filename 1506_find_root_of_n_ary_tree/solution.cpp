// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

#include <unordered_map>
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
    Node* findRoot(std::vector<Node*> tree) {
        int value = 0;
        std::unordered_map<int, Node*> nodes;
        for (Node* node : tree) {
            nodes[node->val] = node;
            value ^= node->val;
            for (Node* child : node->children) {
                value ^= child->val;
            }
        }
        return nodes[value];
    }
};
