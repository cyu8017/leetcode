// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* first = head;
        for (int i = 0; i < k - 1; i++) {
            first = first->next;
        }
        ListNode* fast = first;
        ListNode* second = head;
        while (fast->next) {
            fast = fast->next;
            second = second->next;
        }
        int temp = first->val;
        first->val = second->val;
        second->val = temp;
        return head;
    }
};
