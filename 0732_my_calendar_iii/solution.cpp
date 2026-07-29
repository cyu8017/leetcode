// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

#include <algorithm>
#include <map>

class MyCalendarThree {
public:
    MyCalendarThree() = default;

    int book(int startTime, int endTime) {
        ++delta_[startTime];
        --delta_[endTime];
        int current = 0;
        int best = 0;
        for (auto& [_, change] : delta_) {
            current += change;
            best = std::max(best, current);
        }
        return best;
    }

private:
    std::map<int, int> delta_;
};
