// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

#include <algorithm>
#include <vector>

class Solution {
public:
    int earliestTime(std::vector<std::vector<int>>& tasks) {
        int ans = 200;
        for (auto& task : tasks) ans = std::min(ans, task[0] + task[1]);
        return ans;
    }
};
