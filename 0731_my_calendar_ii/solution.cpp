// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

#include <algorithm>
#include <vector>

class MyCalendarTwo {
public:
    MyCalendarTwo() = default;

    bool book(int startTime, int endTime) {
        for (auto [start, end] : overlaps_) {
            if (start < endTime && startTime < end) {
                return false;
            }
        }
        for (auto [start, end] : booked_) {
            if (start < endTime && startTime < end) {
                overlaps_.push_back({std::max(start, startTime), std::min(end, endTime)});
            }
        }
        booked_.push_back({startTime, endTime});
        return true;
    }

private:
    std::vector<std::pair<int, int>> booked_;
    std::vector<std::pair<int, int>> overlaps_;
};
