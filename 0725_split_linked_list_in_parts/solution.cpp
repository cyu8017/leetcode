// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    std::vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int length = 0;
        for (ListNode* node = head; node; node = node->next) {
            ++length;
        }
        int partSize = length / k;
        int extra = length % k;
        std::vector<ListNode*> result;
        ListNode* current = head;
        for (int i = 0; i < k; ++i) {
            result.push_back(current);
            int size = partSize + (i < extra ? 1 : 0);
            for (int j = 0; j < size - 1 && current; ++j) {
                current = current->next;
            }
            if (current) {
                ListNode* nxt = current->next;
                current->next = nullptr;
                current = nxt;
            }
        }
        return result;
    }
};
