// LeetCode 0986 - Interval List Intersections
// https://leetcode.com/problems/interval-list-intersections/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> intervalIntersection(std::vector<std::vector<int>>& firstList,
                                                       std::vector<std::vector<int>>& secondList) {
        int i = 0, j = 0;
        std::vector<std::vector<int>> ans;
        while (i < (int)firstList.size() && j < (int)secondList.size()) {
            int lo = std::max(firstList[i][0], secondList[j][0]);
            int hi = std::min(firstList[i][1], secondList[j][1]);
            if (lo <= hi) ans.push_back({lo, hi});
            if (firstList[i][1] < secondList[j][1]) i++;
            else j++;
        }
        return ans;
    }
};
