// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

#include <numeric>
#include <vector>

class Solution {
public:
    int subarrayGCD(std::vector<int>& nums, int k) {
        int ans = 0, n = (int)nums.size();
        for (int i = 0; i < n; i++) {
            int g = 0;
            for (int j = i; j < n; j++) {
                g = std::gcd(g, nums[j]);
                if (g < k) break;
                if (g == k) ans++;
            }
        }
        return ans;
    }
};
