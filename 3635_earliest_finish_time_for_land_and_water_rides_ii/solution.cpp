// LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
    int calc(std::vector<int>& a1, std::vector<int>& t1, std::vector<int>& a2, std::vector<int>& t2) {
        int minEnd = INT_MAX;
        for (int i = 0; i < (int)a1.size(); i++) minEnd = std::min(minEnd, a1[i] + t1[i]);
        int ans = INT_MAX;
        for (int i = 0; i < (int)a2.size(); i++) ans = std::min(ans, std::max(minEnd, a2[i]) + t2[i]);
        return ans;
    }

public:
    int earliestFinishTime(std::vector<int>& landStartTime, std::vector<int>& landDuration,
                           std::vector<int>& waterStartTime, std::vector<int>& waterDuration) {
        return std::min(calc(landStartTime, landDuration, waterStartTime, waterDuration),
                        calc(waterStartTime, waterDuration, landStartTime, landDuration));
    }
};
