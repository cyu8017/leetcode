// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

#include <numeric>
#include <vector>

class Solution {
public:
    int clumsy(int n) {
        std::vector<int> stack{n};
        --n;
        int op = 0;
        while (n) {
            if (op % 4 == 0) {
                int top = stack.back();
                stack.pop_back();
                stack.push_back(top * n);
            } else if (op % 4 == 1) {
                int top = stack.back();
                stack.pop_back();
                stack.push_back(top / n);
            } else if (op % 4 == 2) {
                stack.push_back(n);
            } else {
                stack.push_back(-n);
            }
            --n;
            ++op;
        }
        return std::accumulate(stack.begin(), stack.end(), 0);
    }
};

