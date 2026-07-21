// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minPairSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int answer = 0;
        int n = static_cast<int>(nums.size());
        for (int i = 0; i < n / 2; i++) {
            answer = std::max(answer, nums[i] + nums[n - 1 - i]);
        }
        return answer;
    }
};
