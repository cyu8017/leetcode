// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool canAttendMeetings(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& left, const std::vector<int>& right) {
            return left[0] < right[0];
        });
        for (size_t index = 1; index < intervals.size(); index++) {
            if (intervals[index][0] < intervals[index - 1][1]) {
                return false;
            }
        }
        return true;
    }
};
