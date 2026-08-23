// LeetCode 0352 - Data Stream as Disjoint Intervals
// https://leetcode.com/problems/data-stream-as-disjoint-intervals/

#include <algorithm>
#include <vector>

class SummaryRanges {
    std::vector<std::vector<int>> intervals_;

public:
    SummaryRanges() {}

    void addNum(int value) {
        std::vector<int> newInterval = {value, value};
        std::vector<std::vector<int>> merged;
        bool inserted = false;

        for (const auto& interval : intervals_) {
            if (interval[1] < value - 1) {
                merged.push_back(interval);
            } else if (interval[0] > value + 1) {
                if (!inserted) {
                    merged.push_back(newInterval);
                    inserted = true;
                }
                merged.push_back(interval);
            } else {
                newInterval[0] = std::min(newInterval[0], interval[0]);
                newInterval[1] = std::max(newInterval[1], interval[1]);
            }
        }

        if (!inserted) {
            merged.push_back(newInterval);
        }

        intervals_ = merged;
    }

    std::vector<std::vector<int>> getIntervals() {
        return intervals_;
    }
};
