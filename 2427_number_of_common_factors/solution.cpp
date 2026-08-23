// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

#include <numeric>

class Solution {
public:
    int commonFactors(int a, int b) {
        int g = std::gcd(a, b);
        int ans = 0;
        for (int i = 1; i * i <= g; i++) {
            if (g % i == 0) {
                ans++;
                if (i * i != g) ans++;
            }
        }
        return ans;
    }
};
