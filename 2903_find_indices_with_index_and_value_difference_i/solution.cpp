// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> findIndices(std::vector<int>& nums, int indexDifference, int valueDifference) {
        int n = (int)nums.size();
        for (int i = 0; i < n; i++)
            for (int j = i; j < n; j++) {
                int di = std::abs(j - i), dv = std::abs(nums[i] - nums[j]);
                if (di >= indexDifference && dv >= valueDifference) return {i, j};
            }
        return {-1, -1};
    }
};
