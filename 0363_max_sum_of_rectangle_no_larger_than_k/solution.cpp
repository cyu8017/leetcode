// LeetCode 0363 - Max Sum of Rectangle No Larger Than K
// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxSumSubmatrix(std::vector<std::vector<int>>& matrix, int k) {
        int rows = static_cast<int>(matrix.size());
        int cols = rows ? static_cast<int>(matrix[0].size()) : 0;
        int result = INT_MIN;

        for (int top = 0; top < rows; ++top) {
            std::vector<int> colSums(cols, 0);
            for (int bottom = top; bottom < rows; ++bottom) {
                std::vector<int> prefixSums = {0};
                int running = 0;

                for (int col = 0; col < cols; ++col) {
                    colSums[col] += matrix[bottom][col];
                    running += colSums[col];

                    auto iterator = std::lower_bound(prefixSums.begin(), prefixSums.end(), running - k);
                    if (iterator != prefixSums.end()) {
                        result = std::max(result, running - *iterator);
                    }

                    auto insertPos = std::lower_bound(prefixSums.begin(), prefixSums.end(), running);
                    prefixSums.insert(insertPos, running);
                }
            }
        }

        return result;
    }
};
