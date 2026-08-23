// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

#include <algorithm>
#include <cstdint>
#include <functional>
#include <vector>

class Solution {
public:
    long long minPartitionScore(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int64_t> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        auto value = [&](int left, int right) {
            int64_t sum = prefix[right] - prefix[left];
            return sum * (sum + 1) / 2;
        };
        const int64_t INF = 1LL << 62;
        std::vector<int64_t> previous(n + 1, INF);
        previous[0] = 0;
        for (int parts = 1; parts <= k; parts++) {
            std::vector<int64_t> current(n + 1, INF);
            std::function<void(int, int, int, int)> compute = [&](int lo, int hi, int optLo, int optHi) {
                if (lo > hi) return;
                int mid = (lo + hi) / 2;
                int bestIndex = -1;
                int end = std::min(optHi, mid - 1);
                for (int split = optLo; split <= end; split++) {
                    if (previous[split] == INF) continue;
                    int64_t candidate = previous[split] + value(split, mid);
                    if (candidate < current[mid]) {
                        current[mid] = candidate;
                        bestIndex = split;
                    }
                }
                if (bestIndex == -1) bestIndex = optLo;
                compute(lo, mid - 1, optLo, bestIndex);
                compute(mid + 1, hi, bestIndex, optHi);
            };
            compute(parts, n, parts - 1, n - 1);
            previous = std::move(current);
        }
        return previous[n];
    }
};
