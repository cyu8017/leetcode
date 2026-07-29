// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int cherryPickup(std::vector<std::vector<int>>& grid) {
        n_ = static_cast<int>(grid.size());
        grid_ = &grid;
        memo_.assign(n_, std::vector<std::vector<int>>(n_, std::vector<int>(n_, INT_MIN)));
        return std::max(0, dp(0, 0, 0));
    }

private:
    int n_;
    std::vector<std::vector<int>>* grid_;
    std::vector<std::vector<std::vector<int>>> memo_;

    int dp(int r1, int c1, int c2) {
        int r2 = r1 + c1 - c2;
        if (r1 >= n_ || c1 >= n_ || r2 >= n_ || c2 >= n_ || (*grid_)[r1][c1] == -1 ||
            (*grid_)[r2][c2] == -1) {
            return -1000000000;
        }
        if (r1 == n_ - 1 && c1 == n_ - 1) {
            return (*grid_)[r1][c1];
        }
        int& cached = memo_[r1][c1][c2];
        if (cached != INT_MIN) {
            return cached;
        }
        int cherries = (*grid_)[r1][c1];
        if (r1 != r2 || c1 != c2) {
            cherries += (*grid_)[r2][c2];
        }
        cherries += std::max({dp(r1 + 1, c1, c2), dp(r1, c1 + 1, c2), dp(r1 + 1, c1, c2 + 1),
                              dp(r1, c1 + 1, c2 + 1)});
        return cached = cherries;
    }
};
