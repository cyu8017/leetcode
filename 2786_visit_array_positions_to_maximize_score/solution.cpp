// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& nums, int x) {
        long long NEG = -(1LL << 60);
        long long even = nums[0], odd = nums[0];
        if (nums[0] % 2 == 0) odd = NEG;
        else even = NEG;
        for (int i = 1; i < (int)nums.size(); i++) {
            long long v = nums[i];
            if (nums[i] % 2 == 0) even = std::max(even + v, odd + v - x);
            else odd = std::max(odd + v, even + v - x);
        }
        return std::max(even, odd);
    }
};
