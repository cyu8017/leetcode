// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minimumDifference(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int ans = INT_MAX;
        for (int i = 0; i + k - 1 < (int)nums.size(); i++) {
            ans = std::min(ans, nums[i + k - 1] - nums[i]);
        }
        return ans;
    }
};
