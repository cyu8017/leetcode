// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int shipWithinDays(std::vector<int>& weights, int days) {
        int lo = *std::max_element(weights.begin(), weights.end());
        int hi = std::accumulate(weights.begin(), weights.end(), 0);
        auto can = [&](int cap) {
            int need = 1, cur = 0;
            for (int w : weights) {
                if (cur + w > cap) {
                    ++need;
                    cur = 0;
                }
                cur += w;
            }
            return need <= days;
        };
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};

