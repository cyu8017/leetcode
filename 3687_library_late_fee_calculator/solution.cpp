// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

#include <vector>

class Solution {
public:
    int lateFee(std::vector<int>& daysLate) {
        auto f = [](int x) {
            if (x == 1) return 1;
            if (x > 5) return 3 * x;
            return 2 * x;
        };
        int ans = 0;
        for (int x : daysLate) ans += f(x);
        return ans;
    }
};
