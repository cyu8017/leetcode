// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minConnectedGroups(std::vector<std::vector<int>>& intervals, int k) {
        std::sort(intervals.begin(), intervals.end());
        std::vector<std::vector<int>> merged;
        for (auto& it : intervals) {
            if (merged.empty() || it[0] > merged.back()[1]) merged.push_back({it[0], it[1]});
            else if (it[1] > merged.back()[1]) merged.back()[1] = it[1];
        }
        int m = (int)merged.size();
        int ans = m;
        for (int i = 0; i < m; i++) {
            int end = merged[i][1] + k;
            int j = i;
            while (j < m && merged[j][0] <= end) j++;
            int groups = i + 1 + (m - j);
            if (groups < ans) ans = groups;
        }
        return ans;
    }
};
