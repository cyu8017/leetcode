// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int sumCounts(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            std::unordered_set<int> seen;
            for (int j = i; j < n; j++) {
                seen.insert(nums[j]);
                int d = (int)seen.size();
                ans += d * d;
            }
        }
        return ans;
    }
};
