// LeetCode 3897 - Maximum Value Of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

#include <algorithm>
#include <utility>
#include <vector>

class Solution {
    static constexpr int MOD = 1000000007;

    static int group(const std::pair<int, int>& p) {
        if (p.second == 0) return 0;
        if (p.first > 0) return 1;
        return 2;
    }

public:
    int maxValue(std::vector<int>& nums1, std::vector<int>& nums0) {
        int n = (int)nums1.size();
        std::vector<std::pair<int, int>> pairs(n);
        int b = 0;
        for (int i = 0; i < n; i++) {
            pairs[i] = {nums1[i], nums0[i]};
            b += nums1[i] + nums0[i];
        }
        std::sort(pairs.begin(), pairs.end(), [](const auto& a, const auto& b) {
            int g1 = group(a), g2 = group(b);
            if (g1 != g2) return g1 < g2;
            if (g1 == 0) return a.first > b.first;
            if (g1 == 1) {
                if (a.first != b.first) return a.first > b.first;
                return a.second < b.second;
            }
            return a.second < b.second;
        });
        std::vector<int> p(b);
        p[0] = 1;
        for (int i = 1; i < b; i++) p[i] = (int)(2LL * p[i - 1] % MOD);
        int ans = 0;
        b--;
        for (auto& pr : pairs) {
            int cnt1 = pr.first, cnt0 = pr.second;
            while (cnt1 > 0) {
                ans = (ans + p[b]) % MOD;
                b--;
                cnt1--;
            }
            b -= cnt0;
        }
        return ans;
    }
};
