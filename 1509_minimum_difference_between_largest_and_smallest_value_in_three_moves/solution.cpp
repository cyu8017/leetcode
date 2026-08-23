// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minDifference(std::vector<int>& nums) {
        if (nums.size() <= 4) {
            return 0;
        }
        std::sort(nums.begin(), nums.end());
        int answer = INT_MAX;
        for (int i = 0; i < 4; ++i) {
            answer = std::min(answer, nums[nums.size() - 4 + i] - nums[i]);
        }
        return answer;
    }
};
