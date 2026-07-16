// LeetCode 0234 - Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

struct ListNode {
    int val;
    struct ListNode* next;
};

bool isPalindrome(struct ListNode* head) {
    if (!head || !head->next) {
        return true;
    }

    struct ListNode* slow = head;
    struct ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    struct ListNode* prev = NULL;
    while (slow) {
        struct ListNode* next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    struct ListNode* left = head;
    struct ListNode* right = prev;
    while (right) {
        if (left->val != right->val) {
            return false;
        }
        left = left->next;
        right = right->next;
    }
    return true;
}
