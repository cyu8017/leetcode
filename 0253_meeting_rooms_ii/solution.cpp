// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minMeetingRooms(std::vector<std::vector<int>>& intervals) {
        std::vector<int> starts;
        std::vector<int> ends;
        starts.reserve(intervals.size());
        ends.reserve(intervals.size());
        for (const auto& interval : intervals) {
            starts.push_back(interval[0]);
            ends.push_back(interval[1]);
        }
        std::sort(starts.begin(), starts.end());
        std::sort(ends.begin(), ends.end());

        int rooms = 0;
        int maxRooms = 0;
        size_t startIndex = 0;
        size_t endIndex = 0;
        while (startIndex < starts.size()) {
            if (starts[startIndex] < ends[endIndex]) {
                rooms += 1;
                maxRooms = std::max(maxRooms, rooms);
                startIndex += 1;
            } else {
                rooms -= 1;
                endIndex += 1;
            }
        }
        return maxRooms;
    }
};
