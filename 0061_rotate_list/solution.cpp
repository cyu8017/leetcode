// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next) {
            return head;
        }

        ListNode* tail = head;
        int length = 1;
        while (tail->next) {
            tail = tail->next;
            length++;
        }

        tail->next = head;
        k %= length;
        if (k == 0) {
            tail->next = nullptr;
            return head;
        }

        int steps = length - k;
        ListNode* new_tail = head;
        for (int i = 0; i < steps - 1; ++i) {
            new_tail = new_tail->next;
        }

        ListNode* new_head = new_tail->next;
        new_tail->next = nullptr;
        return new_head;
    }
};
