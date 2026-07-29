// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int kConcatenationMaxSum(std::vector<int>& arr, int k) {
        const int MOD = 1e9 + 7;
        auto kadane = [](const std::vector<int>& nums) {
            long long best = 0, cur = 0;
            for (int x : nums) {
                cur = std::max(0LL, cur + x);
                best = std::max(best, cur);
            }
            return best;
        };
        long long one = kadane(arr);
        if (k == 1) return static_cast<int>(one % MOD);
        std::vector<int> two = arr;
        two.insert(two.end(), arr.begin(), arr.end());
        long long twoBest = kadane(two);
        long long total = std::accumulate(arr.begin(), arr.end(), 0LL);
        if (total > 0) return static_cast<int>(std::max(one, twoBest + total * (k - 2)) % MOD);
        return static_cast<int>(std::max(one, twoBest) % MOD);
    }
};
