// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

#include <vector>

class Solution {
public:
    int maxNumberOfAlloys(int n, int k, int budget, std::vector<std::vector<int>>& composition,
                          std::vector<int>& stock, std::vector<int>& cost) {
        (void)k;
        auto ok = [&](long long machines) {
            for (auto& comp : composition) {
                long long spend = 0;
                for (int i = 0; i < n; i++) {
                    long long need = machines * comp[i] - stock[i];
                    if (need > 0) spend += need * cost[i];
                }
                if (spend <= budget) return true;
            }
            return false;
        };
        long long lo = 0, hi = 1000000000LL, ans = 0;
        while (lo <= hi) {
            long long mid = (lo + hi) / 2;
            if (ok(mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return (int)ans;
    }
};
