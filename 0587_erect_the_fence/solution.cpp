// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

#include <algorithm>
#include <set>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> outerTrees(std::vector<std::vector<int>>& trees) {
        std::vector<std::vector<int>> points = trees;
        std::sort(points.begin(), points.end());
        if (points.size() <= 1) {
            return points;
        }

        auto build = [this](const std::vector<std::vector<int>>& ordered) {
            std::vector<std::vector<int>> hull;
            for (const std::vector<int>& point : ordered) {
                while (hull.size() >= 2 &&
                       cross(hull[hull.size() - 2], hull[hull.size() - 1], point) < 0) {
                    hull.pop_back();
                }
                hull.push_back(point);
            }
            return hull;
        };

        std::vector<std::vector<int>> lower = build(points);
        std::vector<std::vector<int>> reversed(points.rbegin(), points.rend());
        std::vector<std::vector<int>> upper = build(reversed);

        std::set<std::vector<int>> unique;
        for (size_t i = 0; i + 1 < lower.size(); ++i) {
            unique.insert(lower[i]);
        }
        for (size_t i = 0; i + 1 < upper.size(); ++i) {
            unique.insert(upper[i]);
        }
        return std::vector<std::vector<int>>(unique.begin(), unique.end());
    }

private:
    long long cross(const std::vector<int>& o, const std::vector<int>& a,
                    const std::vector<int>& b) {
        return 1LL * (a[0] - o[0]) * (b[1] - o[1]) - 1LL * (a[1] - o[1]) * (b[0] - o[0]);
    }
};
