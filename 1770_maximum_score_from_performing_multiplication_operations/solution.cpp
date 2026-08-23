// LeetCode 1770 - Maximum Score from Performing Multiplication Operations
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumScore(std::vector<int>& nums, std::vector<int>& multipliers) {
        int n = (int)nums.size();
        int m = (int)multipliers.size();
        std::vector<int> next(m + 1, 0);
        for (int i = m - 1; i >= 0; i--) {
            std::vector<int> cur(m + 1, 0);
            for (int left = i; left >= 0; left--) {
                int right = n - 1 - (i - left);
                int takeLeft = nums[left] * multipliers[i] + next[left + 1];
                int takeRight = nums[right] * multipliers[i] + next[left];
                cur[left] = std::max(takeLeft, takeRight);
            }
            next = std::move(cur);
        }
        return next[0];
    }
};
