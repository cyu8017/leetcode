// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

#include <vector>

class Solution {
public:
    std::vector<int> getSubarrayBeauty(std::vector<int>& nums, int k, int x) {
        int freq[101] = {};
        std::vector<int> ans(nums.size() - k + 1);
        for (int i = 0; i < (int)nums.size(); i++) {
            freq[nums[i] + 50]++;
            if (i >= k) freq[nums[i - k] + 50]--;
            if (i >= k - 1) {
                int need = x, val = 0;
                for (int j = 0; j < 50; j++) {
                    need -= freq[j];
                    if (need <= 0) { val = j - 50; break; }
                }
                ans[i - k + 1] = val;
            }
        }
        return ans;
    }
};
