// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

#include <algorithm>
#include <vector>

class Solution {
public:
    int totalBeauty(std::vector<int>& nums) {
        const int MOD = 1000000007;
        int mx = 0;
        for (int v : nums) if (v > mx) mx = v;
        std::vector<std::vector<int>> pos(mx + 1);
        for (int i = 0; i < (int)nums.size(); i++) pos[nums[i]].push_back(i);
        std::vector<int> cnt(mx + 1, 0);
        for (int g = 1; g <= mx; g++) {
            std::vector<int> seq;
            for (int m = g; m <= mx; m += g) {
                seq.insert(seq.end(), pos[m].begin(), pos[m].end());
            }
            if (seq.empty()) continue;
            std::sort(seq.begin(), seq.end());
            int ways = 1;
            for (size_t i = 0; i < seq.size(); i++) ways = (int)((ways * 2LL) % MOD);
            cnt[g] = (ways - 1 + MOD) % MOD;
        }
        int ans = 0;
        for (int g = mx; g >= 1; g--) {
            for (int m = 2 * g; m <= mx; m += g) {
                cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD;
            }
            ans = (int)((ans + 1LL * cnt[g] * g) % MOD);
        }
        return ans;
    }
};
