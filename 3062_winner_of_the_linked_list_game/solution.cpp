// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

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

#include <string>

class Solution {
public:
    std::string gameResult(ListNode* head) {
        int odd = 0, even = 0;
        for (; head; head = head->next->next) {
            int a = head->val, b = head->next->val;
            if (a < b) odd++;
            if (a > b) even++;
        }
        if (odd > even) return "Odd";
        if (odd < even) return "Even";
        return "Tie";
    }
};
