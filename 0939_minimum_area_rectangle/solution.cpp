// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

#include <algorithm>
#include <climits>
#include <map>
#include <vector>

class Solution {
public:
    int minAreaRect(std::vector<std::vector<int>>& points) {
        std::map<int, std::vector<int>> byX;
        for (auto& p : points) byX[p[0]].push_back(p[1]);
        std::map<std::pair<int,int>, int> last;
        long long ans = LLONG_MAX;
        for (auto& [x, ys] : byX) {
            std::sort(ys.begin(), ys.end());
            for (int i = 0; i < (int)ys.size(); i++) {
                for (int j = i + 1; j < (int)ys.size(); j++) {
                    auto key = std::make_pair(ys[i], ys[j]);
                    if (last.count(key)) {
                        ans = std::min(ans, 1LL * std::abs(x - last[key]) * (ys[j] - ys[i]));
                    }
                    last[key] = x;
                }
            }
        }
        return ans == LLONG_MAX ? 0 : (int)ans;
    }
};
