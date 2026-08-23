// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long findMaximumScore(std::vector<int>& nums) {
        int64_t ans = 0;
        int maxV = 0;
        for (int i = 0; i < (int)nums.size() - 1; i++) {
            if (nums[i] > maxV) maxV = nums[i];
            ans += maxV;
        }
        return ans;
    }
};
