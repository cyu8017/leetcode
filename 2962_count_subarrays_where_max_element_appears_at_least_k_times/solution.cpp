// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long countSubarrays(std::vector<int>& nums, int k) {
        int mx = *std::max_element(nums.begin(), nums.end());
        long long ans = 0;
        int cnt = 0, left = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            if (nums[right] == mx) cnt++;
            while (cnt >= k) {
                if (nums[left] == mx) cnt--;
                left++;
            }
            ans += left;
        }
        return ans;
    }
};
