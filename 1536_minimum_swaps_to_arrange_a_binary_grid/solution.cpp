// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

#include <vector>

class Solution {
public:
    int minSwaps(std::vector<std::vector<int>>& grid) {
        int n = static_cast<int>(grid.size());
        std::vector<int> zeros;
        zeros.reserve(n);
        for (const auto& row : grid) {
            int count = 0;
            for (int i = n - 1; i >= 0; --i) {
                if (row[i]) {
                    break;
                }
                count += 1;
            }
            zeros.push_back(count);
        }
        int answer = 0;
        for (int i = 0; i < n; ++i) {
            int required = n - i - 1;
            int j = i;
            while (j < n && zeros[j] < required) {
                j += 1;
            }
            if (j == n) {
                return -1;
            }
            answer += j - i;
            int chosen = zeros[j];
            for (int t = j; t > i; --t) {
                zeros[t] = zeros[t - 1];
            }
            zeros[i] = chosen;
        }
        return answer;
    }
};
