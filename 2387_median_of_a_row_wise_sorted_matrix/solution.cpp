// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

#include <vector>

class Solution {
public:
    int matrixMedian(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        int lo = 1, hi = 1000000;
        int need = (m * n) / 2 + 1;
        auto countLE = [&](int x) {
            int cnt = 0;
            for (auto& row : grid) {
                int l = 0, r = n;
                while (l < r) {
                    int mid = (l + r) / 2;
                    if (row[mid] <= x) l = mid + 1;
                    else r = mid;
                }
                cnt += l;
            }
            return cnt;
        };
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (countLE(mid) >= need) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
