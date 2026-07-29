// LeetCode 1943 - Describe the Painting
#include <map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<long long>> splitPainting(std::vector<std::vector<int>>& segments) {
        std::map<int, long long> diff;
        for (auto& seg : segments) {
            diff[seg[0]] += seg[2];
            diff[seg[1]] -= seg[2];
        }
        std::vector<int> points;
        for (auto& [p, _] : diff) points.push_back(p);
        std::vector<std::vector<long long>> ans;
        long long cur = 0;
        for (int i = 0; i + 1 < (int)points.size(); i++) {
            cur += diff[points[i]];
            if (cur) ans.push_back({points[i], points[i + 1], cur});
        }
        return ans;
    }
};
