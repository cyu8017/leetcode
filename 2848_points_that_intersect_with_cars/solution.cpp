// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

#include <vector>

class Solution {
public:
    int numberOfPoints(std::vector<std::vector<int>>& nums) {
        int cov[102] = {};
        for (auto& r : nums)
            for (int x = r[0]; x <= r[1]; x++) cov[x] = 1;
        int ans = 0;
        for (int v : cov) ans += v;
        return ans;
    }
};
