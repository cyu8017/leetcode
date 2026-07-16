// LeetCode 0369 - Plus One Linked List
// https://leetcode.com/problems/plus-one-linked-list/

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* plusOne(ListNode* head) {
        ListNode sentinel(0, head);
        ListNode* notNine = &sentinel;
        ListNode* node = head;

        while (node != nullptr) {
            if (node->val != 9) {
                notNine = node;
            }
            node = node->next;
        }

        notNine->val += 1;
        node = notNine->next;
        while (node != nullptr) {
            node->val = 0;
            node = node->next;
        }

        return sentinel.val == 1 ? &sentinel : sentinel.next;
    }
};
