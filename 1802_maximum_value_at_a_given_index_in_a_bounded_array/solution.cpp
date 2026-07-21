// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        auto minSideSum = [](long long value, long long count) -> long long {
            if (value > count) {
                return (value - 1 + value - count) * count / 2;
            }
            return value * (value - 1) / 2 + (count - value + 1);
        };

        long long lo = 1;
        long long hi = maxSum;
        while (lo < hi) {
            long long mid = (lo + hi + 1) / 2;
            long long total = minSideSum(mid, index) + mid + minSideSum(mid, n - index - 1);
            if (total <= maxSum) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return static_cast<int>(lo);
    }
};
