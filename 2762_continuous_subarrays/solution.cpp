// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

#include <map>
#include <vector>

class Solution {
public:
    long long continuousSubarrays(std::vector<int>& nums) {
        long long ans = 0;
        int left = 0;
        std::map<int, int> freq;
        for (int right = 0; right < (int)nums.size(); right++) {
            freq[nums[right]]++;
            while (freq.rbegin()->first - freq.begin()->first > 2) {
                if (--freq[nums[left]] == 0) freq.erase(nums[left]);
                left++;
            }
            ans += right - left + 1;
        }
        return ans;
    }
};
