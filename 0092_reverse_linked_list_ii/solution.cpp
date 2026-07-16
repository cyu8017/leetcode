// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) {
            return head;
        }

        ListNode dummy(0, head);
        ListNode* before = &dummy;
        for (int i = 0; i < left - 1; ++i) {
            before = before->next;
        }

        ListNode* start = before->next;
        ListNode* current = start->next;

        for (int i = 0; i < right - left; ++i) {
            start->next = current->next;
            current->next = before->next;
            before->next = current;
            current = start->next;
        }

        return dummy.next;
    }
};
