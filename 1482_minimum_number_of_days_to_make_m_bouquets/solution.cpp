#include <algorithm>
#include <vector>

class Solution {
    bool possible(const std::vector<int>& bloomDay, int m, int k, int day) {
        int bouquets = 0, run = 0;
        for (int x : bloomDay) {
            run = x <= day ? run + 1 : 0;
            if (run == k) { ++bouquets; run = 0; }
        }
        return bouquets >= m;
    }
public:
    int minDays(std::vector<int>& bloomDay, int m, int k) {
        if (1LL * m * k > (long long)bloomDay.size()) return -1;
        int lo = *std::min_element(bloomDay.begin(), bloomDay.end());
        int hi = *std::max_element(bloomDay.begin(), bloomDay.end());
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (possible(bloomDay, m, k, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
