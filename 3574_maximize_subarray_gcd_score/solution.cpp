// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

#include <algorithm>
#include <climits>
#include <numeric>
#include <vector>

class Solution {
public:
    long long maxGCDScore(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> cnt(n);
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (x % 2 == 0) {
                cnt[i]++;
                x /= 2;
            }
        }
        long long ans = 0;
        for (int l = 0; l < n; l++) {
            int g = 0, mi = INT_MAX, t = 0;
            for (int r = l; r < n; r++) {
                g = std::gcd(g, nums[r]);
                if (cnt[r] < mi) {
                    mi = cnt[r];
                    t = 1;
                } else if (cnt[r] == mi) {
                    t++;
                }
                long long score = 1LL * g * (r - l + 1);
                if (t <= k) score *= 2;
                ans = std::max(ans, score);
            }
        }
        return ans;
    }
};
