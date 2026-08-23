// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

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

#include <unordered_map>

class Solution {
public:
    ListNode* frequenciesOfElements(ListNode* head) {
        std::unordered_map<int, int> cnt;
        for (; head; head = head->next) cnt[head->val]++;
        ListNode dummy;
        for (auto& [_, val] : cnt) {
            (void)_;
            dummy.next = new ListNode(val, dummy.next);
        }
        return dummy.next;
    }
};
