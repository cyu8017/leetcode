// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

#include <vector>

class Solution {
public:
    std::vector<int> countPoints(std::vector<std::vector<int>>& points, std::vector<std::vector<int>>& queries) {
        std::vector<int> result;
        result.reserve(queries.size());
        for (const auto& query : queries) {
            int xq = query[0];
            int yq = query[1];
            int radiusSq = query[2] * query[2];
            int count = 0;
            for (const auto& point : points) {
                int dx = point[0] - xq;
                int dy = point[1] - yq;
                if (dx * dx + dy * dy <= radiusSq) {
                    ++count;
                }
            }
            result.push_back(count);
        }
        return result;
    }
};
