// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

#include <vector>
#include <algorithm>
#include <utility>

class Solution {
public:
    int maxTrailingZeros(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        using Pair = std::pair<int, int>;
        auto fact = [](int x) {
            int t = 0, f = 0;
            while (x % 2 == 0) { t++; x /= 2; }
            while (x % 5 == 0) { f++; x /= 5; }
            return Pair{t, f};
        };
        std::vector<std::vector<Pair>> left(m, std::vector<Pair>(n));
        std::vector<std::vector<Pair>> up(m, std::vector<Pair>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                Pair p = fact(grid[i][j]);
                left[i][j] = up[i][j] = p;
                if (j > 0) {
                    left[i][j].first += left[i][j - 1].first;
                    left[i][j].second += left[i][j - 1].second;
                }
                if (i > 0) {
                    up[i][j].first += up[i - 1][j].first;
                    up[i][j].second += up[i - 1][j].second;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                Pair cell = fact(grid[i][j]);
                Pair L = left[i][j];
                int Rtwo = left[i][n - 1].first - left[i][j].first + cell.first;
                int Rfive = left[i][n - 1].second - left[i][j].second + cell.second;
                Pair U = up[i][j];
                int Dtwo = up[m - 1][j].first - up[i][j].first + cell.first;
                int Dfive = up[m - 1][j].second - up[i][j].second + cell.second;
                Pair cands[] = {
                    {L.first + U.first - cell.first, L.second + U.second - cell.second},
                    {L.first + Dtwo - cell.first, L.second + Dfive - cell.second},
                    {Rtwo + U.first - cell.first, Rfive + U.second - cell.second},
                    {Rtwo + Dtwo - cell.first, Rfive + Dfive - cell.second},
                };
                for (auto& c : cands) ans = std::max(ans, std::min(c.first, c.second));
            }
        }
        return ans;
    }
};
