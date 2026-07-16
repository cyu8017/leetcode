// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

#include <functional>
#include <vector>

namespace {
std::function<double(double, double)> uniform = [](double low, double) { return low; };
}  // namespace

void set_uniform(std::function<double(double, double)> uniform_fn) {
    uniform = std::move(uniform_fn);
}

class Solution {
    int cols_ = 0;
    int total_ = 0;
    std::vector<int> available_;

    void resetAvailable() {
        available_.resize(total_);
        for (int index = 0; index < total_; ++index) {
            available_[index] = index;
        }
    }

public:
    Solution(int m, int n) : cols_(n), total_(m * n) {
        resetAvailable();
    }

    std::vector<int> flip() {
        int index = static_cast<int>(uniform(0, static_cast<double>(available_.size()) - 1));
        if (index >= static_cast<int>(available_.size())) {
            index = static_cast<int>(available_.size()) - 1;
        }
        const int value = available_[index];
        available_[index] = available_.back();
        available_.pop_back();
        return {value / cols_, value % cols_};
    }

    void reset() {
        resetAvailable();
    }
};
