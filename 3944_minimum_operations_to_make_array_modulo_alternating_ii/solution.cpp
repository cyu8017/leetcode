// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long minOperations(std::vector<int>& nums, int k) {
        std::vector<long long> evenFreq(k), oddFreq(k);
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i % 2 == 0) evenFreq[nums[i] % k]++;
            else oddFreq[nums[i] % k]++;
        }
        auto costs = [&](const std::vector<long long>& freq) {
            std::vector<long long> dbl(2 * k);
            for (int i = 0; i < 2 * k; i++) dbl[i] = freq[i % k];
            std::vector<long long> countPrefix(2 * k + 1), weightedPrefix(2 * k + 1);
            for (int i = 0; i < 2 * k; i++) {
                countPrefix[i + 1] = countPrefix[i] + dbl[i];
                weightedPrefix[i + 1] = weightedPrefix[i] + (long long)i * dbl[i];
            }
            auto rangeStats = [&](int l, int r) {
                return std::pair<long long, long long>{
                    countPrefix[r + 1] - countPrefix[l],
                    weightedPrefix[r + 1] - weightedPrefix[l]
                };
            };
            std::vector<long long> res(k);
            int cw = k / 2, cc = (k - 1) / 2;
            for (int t = 0; t < k; t++) {
                auto [cnt, sum] = rangeStats(t, t + cw);
                res[t] += sum - (long long)t * cnt;
                if (cc > 0) {
                    auto [cnt2, sum2] = rangeStats(t + k - cc, t + k - 1);
                    res[t] += (long long)(t + k) * cnt2 - sum2;
                }
            }
            return res;
        };
        auto evenCost = costs(evenFreq);
        auto oddCost = costs(oddFreq);
        long long best1 = 1LL << 62, best2 = 1LL << 62;
        int bestIndex = -1;
        for (int i = 0; i < k; i++) {
            long long x = oddCost[i];
            if (x < best1) {
                best2 = best1;
                best1 = x;
                bestIndex = i;
            } else if (x < best2) best2 = x;
        }
        long long ans = 1LL << 62;
        for (int x = 0; x < k; x++) {
            long long other = (x == bestIndex) ? best2 : best1;
            ans = std::min(ans, evenCost[x] + other);
        }
        return ans;
    }
};
