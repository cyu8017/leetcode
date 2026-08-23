// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
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
        int mx = 0;
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        while (prev->next) {
            if (prev->next->val >= mx) {
                mx = prev->next->val;
                prev = prev->next;
            } else {
                prev->next = prev->next->next;
            }
        }
        return rev(dummy.next);
    }
};
