// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* insert(ListNode* head, int insertVal) {
        ListNode* node = new ListNode(insertVal);
        if (!head) {
            node->next = node;
            return node;
        }

        ListNode* cur = head;
        while (cur->next && cur->next != head) {
            cur = cur->next;
        }
        cur->next = head;

        ListNode* prev = head;
        ListNode* curr = head->next;
        while (true) {
            if (prev->val <= insertVal && insertVal <= curr->val) {
                break;
            }
            if (prev->val > curr->val && (insertVal >= prev->val || insertVal <= curr->val)) {
                break;
            }
            prev = curr;
            curr = curr->next;
            if (prev == head) {
                break;
            }
        }
        prev->next = node;
        node->next = curr;
        return head;
    }
};
