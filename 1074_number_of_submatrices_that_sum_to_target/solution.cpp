// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int numSubmatrixSumTarget(std::vector<std::vector<int>>& matrix, int target) {
        int rows = static_cast<int>(matrix.size());
        int cols = static_cast<int>(matrix[0].size());
        int ans = 0;
        for (int left = 0; left < cols; ++left) {
            std::vector<int> rowSum(rows, 0);
            for (int right = left; right < cols; ++right) {
                for (int r = 0; r < rows; ++r) {
                    rowSum[r] += matrix[r][right];
                }
                int prefix = 0;
                std::unordered_map<int, int> seen;
                seen[0] = 1;
                for (int val : rowSum) {
                    prefix += val;
                    ans += seen[prefix - target];
                    ++seen[prefix];
                }
            }
        }
        return ans;
    }
};
