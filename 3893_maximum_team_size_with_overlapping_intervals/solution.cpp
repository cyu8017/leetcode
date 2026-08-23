// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumTeamSize(std::vector<int>& startTime, std::vector<int>& endTime) {
        int n = (int)startTime.size();
        std::vector<std::pair<int, int>> intervals(n);
        for (int i = 0; i < n; i++) intervals[i] = {startTime[i], endTime[i]};
        std::vector<int> st = startTime, en = endTime;
        std::sort(st.begin(), st.end());
        std::sort(en.begin(), en.end());
        int ans = 0;
        for (auto& it : intervals) {
            int l = it.first, r = it.second;
            int i = (int)(std::upper_bound(en.begin(), en.end(), l - 1) - en.begin());
            int j = (int)(std::upper_bound(st.begin(), st.end(), r) - st.begin());
            ans = std::max(ans, j - i);
        }
        return ans;
    }
};
