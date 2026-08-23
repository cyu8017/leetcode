// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxScore(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), std::greater<int>());
        long long sum = 0;
        int ans = 0;
        for (int x : nums) {
            sum += x;
            if (sum > 0) ans++;
            else break;
        }
        return ans;
    }
};
