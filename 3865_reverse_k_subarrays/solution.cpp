// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> reverseSubarrays(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        int m = n / k;
        for (int i = 0; i < n; i += m) {
            std::reverse(nums.begin() + i, nums.begin() + i + m);
        }
        return nums;
    }
};
