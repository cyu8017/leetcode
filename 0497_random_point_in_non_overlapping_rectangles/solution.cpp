// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

#include <functional>
#include <vector>

namespace {
std::function<double(double, double)> uniform = [](double low, double) { return low; };
}  // namespace

void set_uniform(std::function<double(double, double)> uniform_fn) {
    uniform = std::move(uniform_fn);
}

class Solution {
    std::vector<std::vector<int>> rects_;
    std::vector<int> prefix_;
    int total_ = 0;

public:
    explicit Solution(std::vector<std::vector<int>>& rects) : rects_(rects) {
        for (const auto& rect : rects_) {
            total_ += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1);
            prefix_.push_back(total_);
        }
    }

    std::vector<int> pick() {
        int index = static_cast<int>(uniform(0, total_));
        if (index >= total_) {
            index = total_ - 1;
        }

        int lo = 0;
        int hi = static_cast<int>(prefix_.size()) - 1;
        while (lo < hi) {
            const int mid = lo + (hi - lo) / 2;
            if (index < prefix_[mid]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        if (lo > 0) {
            index -= prefix_[lo - 1];
        }

        const auto& rect = rects_[lo];
        const int width = rect[2] - rect[0] + 1;
        return {rect[0] + index % width, rect[1] + index / width};
    }
};
