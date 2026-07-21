// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

#include <unordered_map>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* deleteDuplicatesUnsorted(ListNode* head) {
        std::unordered_map<int, int> counts;
        for (ListNode* node = head; node; node = node->next) {
            counts[node->val] += 1;
        }
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        ListNode* node = head;
        while (node) {
            if (counts[node->val] > 1) {
                prev->next = node->next;
                node = node->next;
            } else {
                prev = node;
                node = node->next;
            }
        }
        return dummy.next;
    }
};
