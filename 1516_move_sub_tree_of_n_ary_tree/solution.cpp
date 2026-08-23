// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

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
    Node* moveSubTree(Node* root, Node* p, Node* q) {
        std::unordered_map<Node*, Node*> parent;
        build(root, parent);

        if (parent.count(p) && parent[p] == q) {
            return root;
        }

        Node* p_parent = parent.count(p) ? parent[p] : nullptr;
        Node* q_parent = parent.count(q) ? parent[q] : nullptr;

        if (isAncestor(p, q, parent)) {
            removeChild(q_parent, q);
            if (p_parent == nullptr) {
                root = q;
            } else {
                replaceChild(p_parent, p, q);
            }
            q->children.push_back(p);
        } else {
            if (p_parent == nullptr) {
                root = q;
            } else {
                removeChild(p_parent, p);
            }
            q->children.push_back(p);
        }
        return root;
    }

private:
    void build(Node* node, std::unordered_map<Node*, Node*>& parent) {
        for (Node* child : node->children) {
            parent[child] = node;
            build(child, parent);
        }
    }

    bool isAncestor(Node* a, Node* b, const std::unordered_map<Node*, Node*>& parent) {
        Node* cur = b;
        while (parent.count(cur)) {
            cur = parent.at(cur);
            if (cur == a) {
                return true;
            }
        }
        return false;
    }

    void removeChild(Node* parent, Node* child) {
        auto& kids = parent->children;
        for (auto it = kids.begin(); it != kids.end(); ++it) {
            if (*it == child) {
                kids.erase(it);
                return;
            }
        }
    }

    void replaceChild(Node* parent, Node* old_child, Node* new_child) {
        for (Node*& child : parent->children) {
            if (child == old_child) {
                child = new_child;
                return;
            }
        }
    }
};
