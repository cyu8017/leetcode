// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

#include <array>
#include <map>
#include <vector>

class Solution {
public:
    int minGenerations(std::vector<std::vector<int>>& points, std::vector<int>& target) {
        using Point = std::array<int, 3>;
        Point targetPoint = {target[0], target[1], target[2]};
        std::map<Point, int> generation;
        std::vector<Point> all;
        for (auto& values : points) {
            Point p = {values[0], values[1], values[2]};
            generation[p] = 0;
            all.push_back(p);
        }
        if (generation.count(targetPoint)) return generation[targetPoint];
        for (int current = 1;; current++) {
            int limit = (int)all.size();
            std::vector<Point> added;
            for (int i = 0; i < limit; i++) {
                for (int j = i + 1; j < limit; j++) {
                    if (all[i] == all[j]) continue;
                    Point p = {
                        (all[i][0] + all[j][0]) / 2,
                        (all[i][1] + all[j][1]) / 2,
                        (all[i][2] + all[j][2]) / 2
                    };
                    if (!generation.count(p)) {
                        generation[p] = current;
                        added.push_back(p);
                    }
                }
            }
            if (generation.count(targetPoint)) return generation[targetPoint];
            if (added.empty()) return -1;
            all.insert(all.end(), added.begin(), added.end());
        }
    }
};
