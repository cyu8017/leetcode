// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

#include <vector>

class Solution {
public:
    int countMatchingSubarrays(std::vector<int>& nums, std::vector<int>& pattern) {
        auto f = [](int a, int b) {
            if (a == b) return 0;
            return a < b ? 1 : -1;
        };
        int n = (int)nums.size(), m = (int)pattern.size(), ans = 0;
        for (int i = 0; i < n - m; i++) {
            int ok = 1;
            for (int k = 0; k < m && ok; k++)
                if (f(nums[i + k], nums[i + k + 1]) != pattern[k]) ok = 0;
            ans += ok;
        }
        return ans;
    }
};
