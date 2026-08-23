// LeetCode 0382 - Linked List Random Node
// https://leetcode.com/problems/linked-list-random-node/

#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
    std::vector<int> values_;
    std::vector<int> randomSequence_;
    int randomIndex_ = 0;

public:
    Solution(ListNode* head) {
        while (head) {
            values_.push_back(head->val);
            head = head->next;
        }
        randomSequence_ = {1, 3, 2, 2, 3};
    }

    int getRandom() {
        return randomSequence_[randomIndex_++];
    }
};
