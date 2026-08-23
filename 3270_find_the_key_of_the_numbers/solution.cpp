// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

#include <algorithm>

class Solution {
public:
    int generateKey(int num1, int num2, int num3) {
        int ans = 0, mul = 1;
        for (int t = 0; t < 4; t++) {
            int d = std::min({num1 % 10, num2 % 10, num3 % 10});
            ans += d * mul;
            mul *= 10;
            num1 /= 10; num2 /= 10; num3 /= 10;
        }
        return ans;
    }
};
