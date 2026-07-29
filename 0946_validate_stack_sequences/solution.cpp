// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

#include <vector>

class Solution {
public:
    bool validateStackSequences(std::vector<int>& pushed, std::vector<int>& popped) {
        std::vector<int> stack;
        int j = 0;
        for (int x : pushed) {
            stack.push_back(x);
            while (!stack.empty() && stack.back() == popped[j]) {
                stack.pop_back();
                j++;
            }
        }
        return stack.empty();
    }
};
