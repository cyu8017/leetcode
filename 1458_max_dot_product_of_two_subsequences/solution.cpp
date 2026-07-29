#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxDotProduct(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums2.size();
        std::vector<long long> dp(n + 1, LLONG_MIN / 4);
        for (int a : nums1) {
            auto prev = dp;
            for (int j = 1; j <= n; ++j) {
                long long product = 1LL * a * nums2[j - 1];
                dp[j] = std::max({dp[j - 1], prev[j], product, product + std::max(0LL, prev[j - 1])});
            }
        }
        return (int)dp[n];
    }
};
