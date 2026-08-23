// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

#include <vector>

class Solution {
public:
    int alternateDigitSum(int n) {
        std::vector<int> s;
        while (n > 0) {
            s.push_back(n % 10);
            n /= 10;
        }
        int ans = 0, sign = 1;
        for (int i = (int)s.size() - 1; i >= 0; --i) {
            ans += sign * s[i];
            sign = -sign;
        }
        return ans;
    }
};
