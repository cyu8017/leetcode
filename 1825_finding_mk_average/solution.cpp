// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

#include <algorithm>
#include <deque>
#include <numeric>
#include <vector>

class MKAverage {
public:
    MKAverage(int m, int k) : m_(m), k_(k) {}

    void addElement(int num) {
        stream_.push_back(num);
    }

    int calculateMKAverage() {
        if (static_cast<int>(stream_.size()) < m_) {
            return -1;
        }
        std::vector<int> window(stream_.end() - m_, stream_.end());
        std::sort(window.begin(), window.end());
        long long sum = std::accumulate(window.begin() + k_, window.end() - k_, 0LL);
        return static_cast<int>(sum / (m_ - 2 * k_));
    }

private:
    int m_;
    int k_;
    std::deque<int> stream_;
};
