// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long largestPerimeter(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        long long sum = 0;
        for (int v : nums) sum += v;
        for (int i = (int)nums.size() - 1; i >= 2; i--) {
            sum -= nums[i];
            if (sum > nums[i]) return sum + nums[i];
        }
        return -1;
    }
};
