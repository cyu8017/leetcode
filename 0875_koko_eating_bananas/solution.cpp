// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minEatingSpeed(std::vector<int>& piles, int h) {
        int lo = 1, hi = *std::max_element(piles.begin(), piles.end());
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long long hours = 0;
            for (int p : piles) {
                hours += (p + mid - 1) / mid;
            }
            if (hours <= h) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
};
