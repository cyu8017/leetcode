// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

#include <climits>
#include <stack>
#include <vector>

class Solution {
public:
    bool verifyPreorder(std::vector<int>& preorder) {
        long low = LONG_MIN;
        std::stack<int> nodes;

        for (int value : preorder) {
            if (value < low) {
                return false;
            }
            while (!nodes.empty() && nodes.top() < value) {
                low = nodes.top();
                nodes.pop();
            }
            nodes.push(value);
        }

        return true;
    }
};
