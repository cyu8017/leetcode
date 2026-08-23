// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findMinimumTime(std::vector<std::vector<int>>& tasks) {
        std::sort(tasks.begin(), tasks.end(), [](const auto& a, const auto& b) {
            return a[1] < b[1];
        });
        std::vector<char> used(2001, 0);
        int ans = 0;
        for (auto& t : tasks) {
            int start = t[0], end = t[1], dur = t[2];
            int have = 0;
            for (int i = start; i <= end; ++i) if (used[i]) have++;
            int need = dur - have;
            for (int i = end; i >= start && need > 0; --i) {
                if (!used[i]) {
                    used[i] = 1;
                    need--;
                    ans++;
                }
            }
        }
        return ans;
    }
};
