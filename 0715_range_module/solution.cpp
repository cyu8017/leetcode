// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

#include <algorithm>
#include <vector>

class RangeModule {
public:
    RangeModule() = default;

    void addRange(int left, int right) {
        std::vector<std::pair<int, int>> next;
        bool placed = false;
        for (auto [start, end] : intervals_) {
            if (end < left) {
                next.push_back({start, end});
            } else if (right < start) {
                if (!placed) {
                    next.push_back({left, right});
                    placed = true;
                }
                next.push_back({start, end});
            } else {
                left = std::min(left, start);
                right = std::max(right, end);
            }
        }
        if (!placed) {
            next.push_back({left, right});
        }
        intervals_ = std::move(next);
    }

    bool queryRange(int left, int right) {
        for (auto [start, end] : intervals_) {
            if (start <= left && right <= end) {
                return true;
            }
            if (end >= right) {
                break;
            }
        }
        return false;
    }

    void removeRange(int left, int right) {
        std::vector<std::pair<int, int>> next;
        for (auto [start, end] : intervals_) {
            if (end <= left || right <= start) {
                next.push_back({start, end});
            } else {
                if (start < left) {
                    next.push_back({start, left});
                }
                if (right < end) {
                    next.push_back({right, end});
                }
            }
        }
        intervals_ = std::move(next);
    }

private:
    std::vector<std::pair<int, int>> intervals_;
};
