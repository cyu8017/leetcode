// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> minAvailableDuration(std::vector<std::vector<int>>& slots1,
                                          std::vector<std::vector<int>>& slots2, int duration) {
        std::sort(slots1.begin(), slots1.end());
        std::sort(slots2.begin(), slots2.end());
        int i = 0, j = 0;
        while (i < static_cast<int>(slots1.size()) && j < static_cast<int>(slots2.size())) {
            int start = std::max(slots1[i][0], slots2[j][0]);
            int end = std::min(slots1[i][1], slots2[j][1]);
            if (end - start >= duration) {
                return {start, start + duration};
            }
            if (slots1[i][1] < slots2[j][1]) {
                ++i;
            } else {
                ++j;
            }
        }
        return {};
    }
};
