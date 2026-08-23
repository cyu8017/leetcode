// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> findMaximalUncoveredRanges(int n, std::vector<std::vector<int>>& ranges) {
        std::sort(ranges.begin(), ranges.end());
        std::vector<std::vector<int>> ans;
        int cur = 0;
        for (auto& r : ranges) {
            if (r[0] > cur) ans.push_back({cur, r[0] - 1});
            if (r[1] + 1 > cur) cur = r[1] + 1;
        }
        if (cur < n) ans.push_back({cur, n - 1});
        return ans;
    }
};
