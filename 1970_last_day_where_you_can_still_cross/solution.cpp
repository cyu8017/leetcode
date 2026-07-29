// LeetCode 1970 - Last Day Where You Can Still Cross
#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    int latestDayToCross(int row, int col, std::vector<std::vector<int>>& cells) {
        auto can = [&](int day) {
            std::set<std::pair<int, int>> blocked;
            for (int i = 0; i < day; i++) blocked.insert({cells[i][0] - 1, cells[i][1] - 1});
            std::vector<std::pair<int, int>> stack;
            std::set<std::pair<int, int>> seen;
            for (int c = 0; c < col; c++) {
                if (!blocked.count({0, c})) {
                    stack.push_back({0, c});
                    seen.insert({0, c});
                }
            }
            static const int D[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
            while (!stack.empty()) {
                auto [r, c] = stack.back();
                stack.pop_back();
                if (r == row - 1) return true;
                for (auto& d : D) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                        !blocked.count({nr, nc}) && !seen.count({nr, nc})) {
                        seen.insert({nr, nc});
                        stack.push_back({nr, nc});
                    }
                }
            }
            return false;
        };
        int lo = 1, hi = (int)cells.size(), ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (can(mid)) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans;
    }
};
