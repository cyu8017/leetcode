// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxFixedPoints(std::vector<int>& nums) {
        std::vector<int> tails;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i < nums[i]) continue;
            int d = i - nums[i];
            auto it = std::lower_bound(tails.begin(), tails.end(), d);
            if (it == tails.end()) tails.push_back(d);
            else *it = d;
        }
        return (int)tails.size();
    }
};
