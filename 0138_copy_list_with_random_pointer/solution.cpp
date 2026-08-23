// LeetCode 0138 - Copy List with Random Pointer
#include <unordered_map>
using namespace std;
class Node {
public:
    int val; Node *next, *random;
    Node(int value) : val(value), next(nullptr), random(nullptr) {}
};
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        unordered_map<Node*, Node*> copies;
        for (Node* node = head; node; node = node->next) copies[node] = new Node(node->val);
        for (Node* node = head; node; node = node->next) {
            copies[node]->next = node->next ? copies[node->next] : nullptr;
            copies[node]->random = node->random ? copies[node->random] : nullptr;
        }
        return copies[head];
    }
};