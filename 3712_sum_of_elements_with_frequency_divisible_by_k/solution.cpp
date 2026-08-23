// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int sumDivisibleByK(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        int ans = 0;
        for (auto& [x, v] : cnt) {
            if (v % k == 0) ans += x * v;
        }
        return ans;
    }
};
