// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

#include <algorithm>

class Solution {
    int countLe(int m, int n, int x) {
        int count = 0;
        for (int row = 1; row <= m; ++row) {
            count += std::min(x / row, n);
        }
        return count;
    }

public:
    int findKthNumber(int m, int n, int k) {
        int lo = 1;
        int hi = m * n;
        while (lo < hi) {
            const int mid = lo + (hi - lo) / 2;
            if (countLe(m, n, mid) >= k) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
};
