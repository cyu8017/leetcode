// LeetCode 3686 - Number of Stable Subsequences
// https://leetcode.com/problems/number-of-stable-subsequences/

#include <vector>

class Solution {
public:
    int countStableSubsequences(std::vector<int>& nums) {
        const int MOD = 1000000007;
        int a1 = 0, a2 = 0, b1 = 0, b2 = 0;
        for (int x : nums) {
            if (x % 2 == 1) {
                int na1 = (1 + b1 + b2) % MOD;
                int na2 = a1;
                a1 = (a1 + na1) % MOD;
                a2 = (a2 + na2) % MOD;
            } else {
                int nb1 = (1 + a1 + a2) % MOD;
                int nb2 = b1;
                b1 = (b1 + nb1) % MOD;
                b2 = (b2 + nb2) % MOD;
            }
        }
        return (((a1 + a2) % MOD + b1) % MOD + b2) % MOD;
    }
};
