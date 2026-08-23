// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

#include <stack>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> findPermutation(std::string s) {
        std::stack<int> stack;
        std::vector<int> result;
        stack.push(1);
        for (char ch : s) {
            if (ch == 'I') {
                while (!stack.empty()) {
                    result.push_back(stack.top());
                    stack.pop();
                }
            }
            stack.push(static_cast<int>(stack.size() + result.size() + 1));
        }
        while (!stack.empty()) {
            result.push_back(stack.top());
            stack.pop();
        }
        return result;
    }
};
