// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* sortLinkedList(ListNode* head) {
        if (!head) return nullptr;
        ListNode* prev = head;
        ListNode* cur = head->next;
        while (cur) {
            if (cur->val < 0) {
                prev->next = cur->next;
                cur->next = head;
                head = cur;
                cur = prev->next;
            } else {
                prev = cur;
                cur = cur->next;
            }
        }
        return head;
    }
};
