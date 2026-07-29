// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minHeightShelves(std::vector<std::vector<int>>& books, int shelfWidth) {
        const int n = static_cast<int>(books.size());
        std::vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            int width = 0;
            int height = 0;
            dp[i] = INT_MAX;
            for (int j = i; j >= 1; --j) {
                width += books[j - 1][0];
                if (width > shelfWidth) {
                    break;
                }
                height = std::max(height, books[j - 1][1]);
                dp[i] = std::min(dp[i], dp[j - 1] + height);
            }
        }
        return dp[n];
    }
};
