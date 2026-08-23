// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countOfPairs(std::vector<int>& nums) {
        const int mod = 1000000007;
        int n = (int)nums.size();
        int maxV = *std::max_element(nums.begin(), nums.end());
        std::vector<int> dp(maxV + 1, 0);
        for (int a = 0; a <= nums[0]; a++) dp[a] = 1;
        for (int i = 1; i < n; i++) {
            std::vector<int> ndp(maxV + 1, 0);
            std::vector<int> pref(maxV + 2, 0);
            for (int a = 0; a <= maxV; a++) pref[a + 1] = (pref[a] + dp[a]) % mod;
            for (int a2 = 0; a2 <= nums[i]; a2++) {
                int b2 = nums[i] - a2;
                int maxA1 = a2;
                int lim = nums[i - 1] - b2;
                if (lim < maxA1) maxA1 = lim;
                if (maxA1 < 0) continue;
                if (maxA1 > maxV) maxA1 = maxV;
                ndp[a2] = pref[maxA1 + 1];
            }
            dp = ndp;
        }
        int ans = 0;
        for (int v : dp) ans = (ans + v) % mod;
        return ans;
    }
};
