// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

#include <vector>

class Solution {
public:
    int countMajoritySubarrays(std::vector<int>& nums, int target) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = i; j < n; j++) {
                if (nums[j] == target) cnt++;
                if (cnt * 2 > j - i + 1) ans++;
            }
        }
        return ans;
    }
};
