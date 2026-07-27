// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    std::vector<int> nextLargerNodes(ListNode* head) {
        std::vector<int> vals;
        while (head) {
            vals.push_back(head->val);
            head = head->next;
        }
        std::vector<int> ans(vals.size(), 0);
        std::vector<int> stack;
        for (int i = 0; i < static_cast<int>(vals.size()); ++i) {
            while (!stack.empty() && vals[stack.back()] < vals[i]) {
                ans[stack.back()] = vals[i];
                stack.pop_back();
            }
            stack.push_back(i);
        }
        return ans;
    }
};

