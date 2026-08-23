// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

#include <vector>

class Solution {
public:
    long long countAlternatingSubarrays(std::vector<int>& nums) {
        long long ans = 1, s = 1;
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i] != nums[i - 1]) s++;
            else s = 1;
            ans += s;
        }
        return ans;
    }
};
