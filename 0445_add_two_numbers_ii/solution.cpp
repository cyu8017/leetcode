// LeetCode 0445 - Add Two Numbers II
// https://leetcode.com/problems/add-two-numbers-ii/

#include <stack>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        std::stack<int> stack1;
        std::stack<int> stack2;
        while (l1 != nullptr) {
            stack1.push(l1->val);
            l1 = l1->next;
        }
        while (l2 != nullptr) {
            stack2.push(l2->val);
            l2 = l2->next;
        }

        int carry = 0;
        ListNode* head = nullptr;
        while (!stack1.empty() || !stack2.empty() || carry) {
            int total = carry;
            if (!stack1.empty()) {
                total += stack1.top();
                stack1.pop();
            }
            if (!stack2.empty()) {
                total += stack2.top();
                stack2.pop();
            }
            carry = total / 10;
            head = new ListNode(total % 10, head);
        }
        return head;
    }
};
