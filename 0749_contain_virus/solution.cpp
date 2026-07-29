// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    int containVirus(std::vector<std::vector<int>>& isInfected) {
        int m = static_cast<int>(isInfected.size());
        int n = static_cast<int>(isInfected[0].size());
        int walls = 0;
        while (true) {
            std::set<std::pair<int, int>> seen;
            std::vector<std::set<std::pair<int, int>>> regions;
            std::vector<std::set<std::pair<int, int>>> frontiers;
            std::vector<int> perimeters;

            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (isInfected[i][j] == 1 && !seen.count({i, j})) {
                        std::vector<std::pair<int, int>> stack{{i, j}};
                        seen.insert({i, j});
                        std::set<std::pair<int, int>> region;
                        std::set<std::pair<int, int>> frontier;
                        int perimeter = 0;
                        while (!stack.empty()) {
                            auto [r, c] = stack.back();
                            stack.pop_back();
                            region.insert({r, c});
                            static const int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
                            for (auto& d : dirs) {
                                int nr = r + d[0];
                                int nc = c + d[1];
                                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                                    continue;
                                }
                                if (isInfected[nr][nc] == 1 && !seen.count({nr, nc})) {
                                    seen.insert({nr, nc});
                                    stack.push_back({nr, nc});
                                } else if (isInfected[nr][nc] == 0) {
                                    frontier.insert({nr, nc});
                                    ++perimeter;
                                }
                            }
                        }
                        regions.push_back(std::move(region));
                        frontiers.push_back(std::move(frontier));
                        perimeters.push_back(perimeter);
                    }
                }
            }

            if (regions.empty()) {
                break;
            }
            int quarantine = 0;
            for (int i = 1; i < static_cast<int>(regions.size()); ++i) {
                if (frontiers[i].size() > frontiers[quarantine].size()) {
                    quarantine = i;
                }
            }
            if (frontiers[quarantine].empty()) {
                break;
            }
            walls += perimeters[quarantine];
            for (auto [r, c] : regions[quarantine]) {
                isInfected[r][c] = -1;
            }
            for (int index = 0; index < static_cast<int>(frontiers.size()); ++index) {
                if (index == quarantine) {
                    continue;
                }
                for (auto [r, c] : frontiers[index]) {
                    isInfected[r][c] = 1;
                }
            }
        }
        return walls;
    }
};
