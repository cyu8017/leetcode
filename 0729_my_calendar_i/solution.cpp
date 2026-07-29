// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

#include <vector>

class MyCalendar {
public:
    MyCalendar() = default;

    bool book(int startTime, int endTime) {
        for (auto [start, end] : bookings_) {
            if (start < endTime && startTime < end) {
                return false;
            }
        }
        bookings_.push_back({startTime, endTime});
        return true;
    }

private:
    std::vector<std::pair<int, int>> bookings_;
};
