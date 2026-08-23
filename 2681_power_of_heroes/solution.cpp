// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

#include <vector>
#include <algorithm>

class Solution {
public:
    int sumOfPower(std::vector<int>& nums) {
        const int MOD = 1000000007;
        std::sort(nums.begin(), nums.end());
        long long ans = 0, s = 0;
        for (int x : nums) {
            ans = (ans + (s + x) % MOD * x % MOD * x) % MOD;
            s = (s * 2 + x) % MOD;
        }
        return (int)ans;
    }
};
