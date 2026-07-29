// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

#include <vector>

class Solution {
public:
    std::vector<int> maxSumOfThreeSubarrays(std::vector<int>& nums, int k) {
        const int n = static_cast<int>(nums.size());
        const int windows = n - k + 1;
        std::vector<int> sums(windows, 0);
        int total = 0;
        for (int i = 0; i < k; ++i) {
            total += nums[i];
        }
        sums[0] = total;
        for (int i = 1; i < windows; ++i) {
            total += nums[i + k - 1] - nums[i - 1];
            sums[i] = total;
        }

        std::vector<int> left(windows, 0);
        int best = 0;
        for (int i = 0; i < windows; ++i) {
            if (sums[i] > sums[best]) {
                best = i;
            }
            left[i] = best;
        }

        std::vector<int> right(windows, 0);
        best = windows - 1;
        for (int i = windows - 1; i >= 0; --i) {
            if (sums[i] >= sums[best]) {
                best = i;
            }
            right[i] = best;
        }

        std::vector<int> answer = {0, 0, 0};
        int bestTotal = -1;
        for (int mid = k; mid < windows - k; ++mid) {
            const int l = left[mid - k];
            const int r = right[mid + k];
            const int cur = sums[l] + sums[mid] + sums[r];
            if (cur > bestTotal) {
                bestTotal = cur;
                answer = {l, mid, r};
            }
        }
        return answer;
    }
};
