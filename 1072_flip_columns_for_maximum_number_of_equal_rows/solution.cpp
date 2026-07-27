// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxEqualRowsAfterFlips(std::vector<std::vector<int>>& matrix) {
        std::unordered_map<std::string, int> patterns;
        int best = 0;
        for (const auto& row : matrix) {
            int base = row[0];
            std::string key;
            key.reserve(row.size());
            for (int x : row) {
                key.push_back(static_cast<char>('0' + (x ^ base)));
            }
            best = std::max(best, ++patterns[key]);
        }
        return best;
    }
};
