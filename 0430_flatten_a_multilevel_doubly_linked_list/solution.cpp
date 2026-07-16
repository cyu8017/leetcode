// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;

    Node(int _val = 0, Node* _prev = nullptr, Node* _next = nullptr, Node* _child = nullptr)
        : val(_val), prev(_prev), next(_next), child(_child) {}
};

class Solution {
public:
    Node* flatten(Node* head) {
        Node* current = head;
        while (current != nullptr) {
            if (current->child != nullptr) {
                Node* nextNode = current->next;
                Node* childHead = flatten(current->child);
                current->next = childHead;
                childHead->prev = current;
                Node* tail = childHead;
                while (tail->next != nullptr) {
                    tail = tail->next;
                }
                tail->next = nextNode;
                if (nextNode != nullptr) {
                    nextNode->prev = tail;
                }
                current->child = nullptr;
            }
            current = current->next;
        }
        return head;
    }
};
