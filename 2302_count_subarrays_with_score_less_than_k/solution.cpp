// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

#include <vector>

class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, long long k) {
        long long ans = 0, sum = 0;
        int left = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            sum += nums[right];
            while (sum * (right - left + 1) >= k) {
                sum -= nums[left];
                left++;
            }
            ans += right - left + 1;
        }
        return ans;
    }
};
