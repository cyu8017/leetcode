// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

#include <vector>

class Solution {
public:
    int minChanges(std::vector<int>& nums, int k) {
        std::vector<std::vector<int>> freq(k, std::vector<int>(1024, 0));
        std::vector<int> size(k, 0);
        for (int i = 0; i < (int)nums.size(); i++) {
            freq[i % k][nums[i]]++;
            size[i % k]++;
        }
        const int INF = 1000000000;
        std::vector<int> dp(256, INF);
        dp[0] = 0;
        for (int i = 0; i < k; i++) {
            std::vector<int> ndp(256, INF);
            for (int xv = 0; xv < 256; xv++) {
                int cost = size[i] - freq[i][xv];
                for (int xo = 0; xo < 256; xo++) {
                    if (dp[xo] == INF) {
                        continue;
                    }
                    int key = xo ^ xv;
                    if (dp[xo] + cost < ndp[key]) {
                        ndp[key] = dp[xo] + cost;
                    }
                }
            }
            dp = std::move(ndp);
        }
        return dp[0];
    }
};
