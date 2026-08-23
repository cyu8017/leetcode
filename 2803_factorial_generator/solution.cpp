// LeetCode 2803 - Factorial Generator
// https://leetcode.com/problems/factorial-generator/
// JS generator stand-in returning factorial sequence.

#include <vector>

class Solution {
public:
    std::vector<int> factorialGenerator(int n) {
        std::vector<int> ans;
        int cur = 1;
        for (int i = 1; i <= n; i++) {
            cur *= i;
            ans.push_back(cur);
        }
        return ans;
    }
};
