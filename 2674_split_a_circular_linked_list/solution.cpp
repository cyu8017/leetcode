// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    std::vector<ListNode*> splitCircularLinkedList(ListNode* list) {
        if (!list) return {nullptr, nullptr};
        ListNode *slow = list, *fast = list;
        while (fast->next != list && fast->next->next != list) {
            slow = slow->next;
            fast = fast->next->next;
        }
        if (fast->next->next == list) fast = fast->next;
        ListNode* head2 = slow->next;
        slow->next = list;
        fast->next = head2;
        return {list, head2};
    }
};
