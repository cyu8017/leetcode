// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minDeletionSize(std::vector<std::string>& strs) {
        int m = (int)strs[0].size();
        std::vector<int> dp(m, 1);
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < j; i++) {
                bool ok = true;
                for (const auto& row : strs) {
                    if (row[i] > row[j]) { ok = false; break; }
                }
                if (ok) dp[j] = std::max(dp[j], dp[i] + 1);
            }
        }
        return m - *std::max_element(dp.begin(), dp.end());
    }
};
