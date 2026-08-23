// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minMoves(std::vector<int>& nums, int k) {
        std::vector<long long> adjusted;
        for (int i = 0; i < static_cast<int>(nums.size()); i++) {
            if (nums[i] == 1) {
                adjusted.push_back(i - static_cast<long long>(adjusted.size()));
            }
        }
        int m = static_cast<int>(adjusted.size());
        std::vector<long long> prefix(m + 1, 0);
        for (int i = 0; i < m; i++) {
            prefix[i + 1] = prefix[i] + adjusted[i];
        }
        long long best = LLONG_MAX;
        for (int left = 0; left + k <= m; left++) {
            int right = left + k;
            int mid = left + k / 2;
            long long median = adjusted[mid];
            long long cost = median * (mid - left) - (prefix[mid] - prefix[left]);
            cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1);
            best = std::min(best, cost);
        }
        return static_cast<int>(best);
    }
};
