// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

#include <functional>
#include <vector>

namespace {
std::function<double(double, double)> uniform = [](double low, double) { return low; };
}  // namespace

void set_uniform(std::function<double(double, double)> uniform_fn) {
    uniform = std::move(uniform_fn);
}

class Solution {
    std::vector<int> prefix_;
    int total_ = 0;

    static int bisectRight(const std::vector<int>& values, int target) {
        int low = 0;
        int high = static_cast<int>(values.size()) - 1;
        while (low < high) {
            const int mid = low + (high - low) / 2;
            if (values[mid] <= target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

public:
    explicit Solution(std::vector<int>& w) {
        int runningTotal = 0;
        for (const int weight : w) {
            runningTotal += weight;
            prefix_.push_back(runningTotal);
        }
        total_ = runningTotal;
    }

    int pickIndex() {
        int target = static_cast<int>(uniform(0, total_));
        if (target >= total_) {
            target = total_ - 1;
        }
        return bisectRight(prefix_, target);
    }
};
