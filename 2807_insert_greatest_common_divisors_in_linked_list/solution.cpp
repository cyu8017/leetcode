// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        auto gcd = [](int a, int b) {
            while (b) { int t = a % b; a = b; b = t; }
            return a;
        };
        ListNode* cur = head;
        while (cur && cur->next) {
            int g = gcd(cur->val, cur->next->val);
            ListNode* node = new ListNode(g, cur->next);
            cur->next = node;
            cur = node->next;
        }
        return head;
    }
};
