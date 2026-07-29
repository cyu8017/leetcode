// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

#include <unordered_set>
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
    int numComponents(ListNode* head, std::vector<int>& nums) {
        std::unordered_set<int> present(nums.begin(), nums.end());
        int count = 0;
        bool connected = false;
        while (head) {
            if (present.count(head->val)) {
                if (!connected) {
                    ++count;
                    connected = true;
                }
            } else {
                connected = false;
            }
            head = head->next;
        }
        return count;
    }
};
