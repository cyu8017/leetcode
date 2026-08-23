// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k, int numOperations) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        int ans = 1;
        for (auto& [t, f] : freq) {
            int lo = (int)(std::lower_bound(nums.begin(), nums.end(), t - k) - nums.begin());
            int hi = (int)(std::upper_bound(nums.begin(), nums.end(), t + k) - nums.begin());
            int can = hi - lo;
            int use = can;
            if (use > f + numOperations) use = f + numOperations;
            if (use > ans) ans = use;
        }
        int l = 0;
        for (int r = 0; r < n; r++) {
            while (nums[r] - nums[l] > 2 * k) l++;
            int window = r - l + 1;
            if (window > numOperations) window = numOperations;
            if (window > ans) ans = window;
        }
        return ans;
    }
};
