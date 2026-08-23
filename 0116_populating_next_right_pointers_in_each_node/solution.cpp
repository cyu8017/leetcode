// LeetCode 0116 - Populating Next Right Pointers in Each Node
#include <queue>
class Node { public: int val; Node *left, *right, *next; };
class Solution { public: Node* connect(Node* root) {
    if (!root) return root; std::queue<Node*> q; q.push(root);
    while (!q.empty()) { int n = q.size(); Node* prev = nullptr;
        while (n--) { Node* cur = q.front(); q.pop(); if (prev) prev->next = cur; prev = cur;
            if (cur->left) q.push(cur->left); if (cur->right) q.push(cur->right); }
        prev->next = nullptr;
    } return root;
} };