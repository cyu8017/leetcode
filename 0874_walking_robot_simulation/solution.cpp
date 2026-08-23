// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int robotSim(std::vector<int>& commands, std::vector<std::vector<int>>& obstacles) {
        auto encode = [](int x, int y) {
            return (static_cast<long long>(x + 30000) << 20) | (y + 30000);
        };
        std::unordered_set<long long> blocked;
        for (auto& o : obstacles) {
            blocked.insert(encode(o[0], o[1]));
        }
        const int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int x = 0, y = 0, d = 0, best = 0;
        for (int cmd : commands) {
            if (cmd == -1) {
                d = (d + 1) % 4;
            } else if (cmd == -2) {
                d = (d + 3) % 4;
            } else {
                int dx = dirs[d][0], dy = dirs[d][1];
                for (int step = 0; step < cmd; ++step) {
                    int nx = x + dx, ny = y + dy;
                    if (blocked.count(encode(nx, ny))) {
                        break;
                    }
                    x = nx;
                    y = ny;
                }
                best = std::max(best, x * x + y * y);
            }
        }
        return best;
    }
};
