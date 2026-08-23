// LeetCode 3027 - Find the Number of Ways to Place People II
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int numberOfPairs(std::vector<std::vector<int>>& points) {
        std::sort(points.begin(), points.end(), [](const auto& a, const auto& b) {
            return a[0] < b[0] || (a[0] == b[0] && b[1] < a[1]);
        });
        int ans = 0;
        for (int i = 0; i < (int)points.size(); i++) {
            int y1 = points[i][1];
            int maxY = INT_MIN;
            for (int j = i + 1; j < (int)points.size(); j++) {
                int y2 = points[j][1];
                if (maxY < y2 && y2 <= y1) {
                    maxY = y2;
                    ans++;
                }
            }
        }
        return ans;
    }
};
