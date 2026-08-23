// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

#include <vector>

class Solution {
public:
    std::vector<int> resultsArray(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> ans(n - k + 1);
        for (int i = 0; i <= n - k; i++) {
            bool ok = true;
            for (int j = i + 1; j < i + k; j++) {
                if (nums[j] != nums[j - 1] + 1) { ok = false; break; }
            }
            ans[i] = ok ? nums[i + k - 1] : -1;
        }
        return ans;
    }
};
