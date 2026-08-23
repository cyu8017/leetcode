// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

#include <vector>

class Solution {
public:
    long long subarraysWithXorAtLeastK(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = 0;
            for (int j = i; j < n; j++) {
                x ^= nums[j];
                if (x >= k) ans++;
            }
        }
        return ans;
    }
};
