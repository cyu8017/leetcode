// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

#include <numeric>
#include <vector>

class Solution {
public:
    int maximizeSweetness(std::vector<int>& sweetness, int k) {
        int lo = 1;
        int hi = std::accumulate(sweetness.begin(), sweetness.end(), 0) / (k + 1);
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int pieces = 0, current = 0;
            for (int value : sweetness) {
                current += value;
                if (current >= mid) {
                    ++pieces;
                    current = 0;
                }
            }
            if (pieces >= k + 1) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return hi;
    }
};
