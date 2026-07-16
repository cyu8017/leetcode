// LeetCode 0346 - Moving Average from Data Stream
// https://leetcode.com/problems/moving-average-from-data-stream/

#include <deque>

class MovingAverage {
    int size_;
    std::deque<int> values_;
    long long total_ = 0;

public:
    MovingAverage(int size) : size_(size) {}

    double next(int val) {
        values_.push_back(val);
        total_ += val;
        if (static_cast<int>(values_.size()) > size_) {
            total_ -= values_.front();
            values_.pop_front();
        }
        return static_cast<double>(total_) / static_cast<double>(values_.size());
    }
};
