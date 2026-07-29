// LeetCode 1975 - Maximum Matrix Sum
#include <algorithm>
#include <climits>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long maxMatrixSum(std::vector<std::vector<int>>& matrix) {
        long long total = 0;
        int neg = 0, mn = INT_MAX;
        for (auto& row : matrix) {
            for (int x : row) {
                if (x < 0) neg++;
                int ax = std::abs(x);
                total += ax;
                mn = std::min(mn, ax);
            }
        }
        if (neg % 2 == 0) return total;
        return total - 2LL * mn;
    }
};
