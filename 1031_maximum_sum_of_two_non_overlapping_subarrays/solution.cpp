// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxSumTwoNoOverlap(std::vector<int>& nums, int firstLen, int secondLen) {
        int n = static_cast<int>(nums.size());
        std::vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) prefix[i + 1] = prefix[i] + nums[i];
        auto best = [&](int a, int b) {
            int bestA = 0, ans = 0;
            for (int i = a + b; i <= n; ++i) {
                bestA = std::max(bestA, prefix[i - b] - prefix[i - b - a]);
                ans = std::max(ans, bestA + prefix[i] - prefix[i - b]);
            }
            return ans;
        };
        return std::max(best(firstLen, secondLen), best(secondLen, firstLen));
    }
};

