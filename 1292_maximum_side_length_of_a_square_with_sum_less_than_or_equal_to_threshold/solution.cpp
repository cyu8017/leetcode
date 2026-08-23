// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxSideLength(std::vector<std::vector<int>>& mat, int threshold) {
        const int m = static_cast<int>(mat.size());
        const int n = static_cast<int>(mat[0].size());
        std::vector<std::vector<int>> prefix(m + 1, std::vector<int>(n + 1, 0));
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
            }
        }
        auto possible = [&](int size) {
            for (int r = size; r <= m; ++r) {
                for (int c = size; c <= n; ++c) {
                    int sum = prefix[r][c] - prefix[r - size][c] - prefix[r][c - size] + prefix[r - size][c - size];
                    if (sum <= threshold) {
                        return true;
                    }
                }
            }
            return false;
        };
        int lo = 0, hi = std::min(m, n);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (possible(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
};
