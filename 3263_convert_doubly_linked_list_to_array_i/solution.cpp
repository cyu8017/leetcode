// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

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
    std::vector<int> toArray(Node* head) {
        std::vector<int> ans;
        while (head) {
            ans.push_back(head->val);
            head = head->next;
        }
        return ans;
    }
};
