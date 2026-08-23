// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximizeSquareHoleArea(int n, int m, std::vector<int>& hBars, std::vector<int>& vBars) {
        (void)n; (void)m;
        auto maxGap = [](std::vector<int> bars) {
            if (bars.empty()) return 1;
            std::sort(bars.begin(), bars.end());
            int best = 1, cur = 1;
            for (int i = 1; i < (int)bars.size(); i++) {
                if (bars[i] == bars[i - 1] + 1) cur++;
                else cur = 1;
                if (cur > best) best = cur;
            }
            return best + 1;
        };
        int side = maxGap(hBars);
        int vs = maxGap(vBars);
        if (vs < side) side = vs;
        return side * side;
    }
};
