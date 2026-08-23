// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

#include <vector>

class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node() : val(0), prev(nullptr), next(nullptr) {}
    Node(int x) : val(x), prev(nullptr), next(nullptr) {}
};

class Solution {
public:
    std::vector<int> toArray(Node* node) {
        while (node && node->prev) node = node->prev;
        std::vector<int> ans;
        while (node) {
            ans.push_back(node->val);
            node = node->next;
        }
        return ans;
    }
};
