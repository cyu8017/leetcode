// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxNumOfMarkedIndices(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        int i = 0, ans = 0;
        for (int j = (n + 1) / 2; j < n; ++j) {
            if (2 * nums[i] <= nums[j]) {
                ans += 2;
                i++;
            }
        }
        return ans;
    }
};
