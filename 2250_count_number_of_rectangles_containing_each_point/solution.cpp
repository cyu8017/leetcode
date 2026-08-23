// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> countRectangles(std::vector<std::vector<int>>& rectangles, std::vector<std::vector<int>>& points) {
        std::vector<std::vector<int>> byH(101);
        for (auto& r : rectangles) byH[r[1]].push_back(r[0]);
        for (int h = 1; h <= 100; ++h) std::sort(byH[h].begin(), byH[h].end());
        std::vector<int> ans(points.size());
        for (size_t i = 0; i < points.size(); ++i) {
            int x = points[i][0], y = points[i][1], cnt = 0;
            for (int h = y; h <= 100; ++h) {
                auto& xs = byH[h];
                auto it = std::lower_bound(xs.begin(), xs.end(), x);
                cnt += (int)(xs.end() - it);
            }
            ans[i] = cnt;
        }
        return ans;
    }
};
