#include <vector>

class Node {
public:
    int val;
    std::vector<Node*> children;
    Node() {}
    Node(int _val) { val = _val; }
    Node(int _val, std::vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
public:
    Node* cloneTree(Node* root) {
        if (!root) return nullptr;
        std::vector<Node*> kids;
        for (Node* child : root->children) kids.push_back(cloneTree(child));
        return new Node(root->val, kids);
    }
};
