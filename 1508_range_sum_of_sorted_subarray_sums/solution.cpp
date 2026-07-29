// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

#include <algorithm>
#include <vector>

class Solution {
public:
    int rangeSum(std::vector<int>& nums, int n, int left, int right) {
        std::vector<int> values;
        values.reserve(n * (n + 1) / 2);
        for (int i = 0; i < n; ++i) {
            int total = 0;
            for (int j = i; j < n; ++j) {
                total += nums[j];
                values.push_back(total);
            }
        }
        std::sort(values.begin(), values.end());
        long long sum = 0;
        for (int i = left - 1; i < right; ++i) {
            sum += values[i];
        }
        return static_cast<int>(sum % 1000000007);
    }
};
