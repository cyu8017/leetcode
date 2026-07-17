// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumScore(std::vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<int> stack;
        long long ans = 0;
        for (int i = 0; i <= n; i++) {
            while (!stack.empty() && (i == n || nums[i] < nums[stack.back()])) {
                int mid = stack.back();
                stack.pop_back();
                int left = stack.empty() ? 0 : stack.back() + 1;
                int right = i - 1;
                if (left <= k && k <= right) {
                    ans = std::max(ans, (long long)nums[mid] * (right - left + 1));
                }
            }
            stack.push_back(i);
        }
        return (int)ans;
    }
};
