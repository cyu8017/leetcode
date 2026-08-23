// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int countTrapezoids(std::vector<std::vector<int>>& points) {
        int n = (int)points.size();
        std::unordered_map<double, std::unordered_map<double, int>> cnt1;
        std::unordered_map<int, std::unordered_map<double, int>> cnt2;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = 0; j < i; j++) {
                int x2 = points[j][0], y2 = points[j][1];
                int dx = x2 - x1, dy = y2 - y1;
                double k, b;
                if (dx == 0) {
                    k = 1e9;
                    b = x1;
                } else {
                    k = (double)dy / dx;
                    b = (double)((long long)y1 * dx - (long long)x1 * dy) / dx;
                }
                cnt1[k][b]++;
                int p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000);
                cnt2[p][k]++;
            }
        }
        int ans = 0;
        for (auto& [_, e] : cnt1) {
            int s = 0;
            for (auto& [__, t] : e) {
                ans += s * t;
                s += t;
            }
        }
        for (auto& [_, e] : cnt2) {
            int s = 0;
            for (auto& [__, t] : e) {
                ans -= s * t;
                s += t;
            }
        }
        return ans;
    }
};
