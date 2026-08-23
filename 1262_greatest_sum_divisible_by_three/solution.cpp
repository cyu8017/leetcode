// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxSumDivThree(std::vector<int>& nums) {
        const long long impossible = LLONG_MIN / 4;
        std::vector<long long> dp{0, impossible, impossible};
        for (int value : nums) {
            std::vector<long long> old = dp;
            for (long long total : old) {
                if (total == impossible) {
                    continue;
                }
                int remainder = static_cast<int>((total + value) % 3);
                dp[remainder] = std::max(dp[remainder], total + value);
            }
        }
        return static_cast<int>(dp[0]);
    }
};
