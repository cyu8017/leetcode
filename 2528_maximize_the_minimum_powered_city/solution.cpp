// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxPower(std::vector<int>& stations, int r, int k) {
        int n = (int)stations.size();
        std::vector<long long> diff(n + 1);
        for (int i = 0; i < n; i++) {
            int L = std::max(0, i - r);
            int R = std::min(n - 1, i + r);
            diff[L] += stations[i];
            diff[R + 1] -= stations[i];
        }
        std::vector<long long> power(n);
        long long cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            power[i] = cur;
        }
        auto ok = [&](long long x) {
            std::vector<long long> extra(n + 1);
            long long have = 0, used = 0;
            for (int i = 0; i < n; i++) {
                have += extra[i];
                long long need = x - (power[i] + have);
                if (need > 0) {
                    used += need;
                    if (used > k) return false;
                    have += need;
                    int end = i + 2 * r;
                    if (end + 1 <= n) extra[end + 1] -= need;
                }
            }
            return true;
        };
        long long lo = 0, hi = k;
        for (long long p : power) if (p > hi) hi = p;
        hi += k;
        while (lo < hi) {
            long long mid = (lo + hi + 1) / 2;
            if (ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
