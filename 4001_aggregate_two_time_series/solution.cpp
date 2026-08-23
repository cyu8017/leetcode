// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> aggregateTimeSeries(std::vector<std::vector<int>>& series1,
                                                      std::vector<std::vector<int>>& series2) {
        int m = (int)series1.size(), n = (int)series2.size();
        int i = 0, j = 0;
        std::vector<std::vector<int>> ans;

        while (i < m && j < n) {
            int t1 = series1[i][0], v1 = series1[i][1];
            int t2 = series2[j][0], v2 = series2[j][1];
            if (t1 == t2) {
                ans.push_back({t1, v1 + v2});
                i++;
                j++;
            } else if (t1 < t2) {
                ans.push_back({t1, v1 + v2});
                i++;
            } else {
                ans.push_back({t2, v1 + v2});
                j++;
            }
        }
        while (i < m) {
            ans.push_back(series1[i]);
            i++;
        }
        while (j < n) {
            ans.push_back(series2[j]);
            j++;
        }
        return ans;
    }
};
