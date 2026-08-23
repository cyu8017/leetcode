// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> reconstructMatrix(int upper, int lower, std::vector<int>& colsum) {
        const int n = static_cast<int>(colsum.size());
        std::vector<int> top(n, 0), bottom(n, 0);
        for (int i = 0; i < n; ++i) {
            if (colsum[i] == 2) {
                top[i] = bottom[i] = 1;
                --upper;
                --lower;
            }
        }
        if (upper < 0 || lower < 0) {
            return {};
        }
        for (int i = 0; i < n; ++i) {
            if (colsum[i] == 1) {
                if (upper) {
                    top[i] = 1;
                    --upper;
                } else if (lower) {
                    bottom[i] = 1;
                    --lower;
                } else {
                    return {};
                }
            }
        }
        if (upper == 0 && lower == 0) {
            return {top, bottom};
        }
        return {};
    }
};
