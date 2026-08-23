// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long largestSquareArea(std::vector<std::vector<int>>& bottomLeft, std::vector<std::vector<int>>& topRight) {
        long long ans = 0;
        int n = (int)bottomLeft.size();
        for (int i = 0; i < n; i++) {
            int x1 = bottomLeft[i][0], y1 = bottomLeft[i][1];
            int x2 = topRight[i][0], y2 = topRight[i][1];
            for (int j = i + 1; j < n; j++) {
                int x3 = bottomLeft[j][0], y3 = bottomLeft[j][1];
                int x4 = topRight[j][0], y4 = topRight[j][1];
                int ww = std::min(x2, x4) - std::max(x1, x3);
                int h = std::min(y2, y4) - std::max(y1, y3);
                int e = std::min(ww, h);
                if (e > 0) ans = std::max(ans, (long long)e * e);
            }
        }
        return ans;
    }
};
