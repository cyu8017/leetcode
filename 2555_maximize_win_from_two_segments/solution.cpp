// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/

#include <vector>

class Solution {
public:
    int maximizeWin(std::vector<int>& prizePositions, int k) {
        int n = (int)prizePositions.size();
        std::vector<int> dp(n + 1);
        int ans = 0, left = 0;
        for (int right = 0; right < n; ++right) {
            while (prizePositions[right] - prizePositions[left] > k) left++;
            int cur = right - left + 1;
            if (dp[left] + cur > ans) ans = dp[left] + cur;
            int best = cur;
            if (dp[right] > best) best = dp[right];
            dp[right + 1] = best;
        }
        return ans;
    }
};
