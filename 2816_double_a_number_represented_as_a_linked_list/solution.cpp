// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* doubleIt(ListNode* head) {
        auto rev = [](ListNode* node) {
            ListNode* prev = nullptr;
            while (node) {
                ListNode* nxt = node->next;
                node->next = prev;
                prev = node;
                node = nxt;
            }
            return prev;
        };
        head = rev(head);
        int carry = 0;
        ListNode* cur = head;
        ListNode* prev = nullptr;
        while (cur) {
            int val = cur->val * 2 + carry;
            cur->val = val % 10;
            carry = val / 10;
            prev = cur;
            cur = cur->next;
        }
        if (carry > 0) prev->next = new ListNode(carry);
        return rev(head);
    }
};
