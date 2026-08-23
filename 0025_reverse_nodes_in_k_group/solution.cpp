// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy(0, head);
        ListNode* groupPrevious = &dummy;

        while (true) {
            ListNode* kth = groupPrevious;
            for (int i = 0; i < k; i++) {
                kth = kth->next;
                if (!kth) {
                    return dummy.next;
                }
            }

            ListNode* groupNext = kth->next;
            ListNode* previous = groupNext;
            ListNode* current = groupPrevious->next;

            while (current != groupNext) {
                ListNode* next = current->next;
                current->next = previous;
                previous = current;
                current = next;
            }

            ListNode* tmp = groupPrevious->next;
            groupPrevious->next = kth;
            groupPrevious = tmp;
        }
    }
};
