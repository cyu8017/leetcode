// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

#include <vector>
#include <set>
#include <utility>

class Solution {
public:
    int countLatticePoints(std::vector<std::vector<int>>& circles) {
        std::set<std::pair<int, int>> seen;
        for (auto& c : circles) {
            int x = c[0], y = c[1], r = c[2];
            for (int i = x - r; i <= x + r; ++i)
                for (int j = y - r; j <= y + r; ++j)
                    if ((i - x) * (i - x) + (j - y) * (j - y) <= r * r)
                        seen.insert({i, j});
        }
        return (int)seen.size();
    }
};
