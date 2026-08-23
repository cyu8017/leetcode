// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0, head);
        ListNode* previous = &dummy;

        while (previous->next && previous->next->next) {
            ListNode* first = previous->next;
            ListNode* second = previous->next->next;
            first->next = second->next;
            second->next = first;
            previous->next = second;
            previous = first;
        }

        return dummy.next;
    }
};
