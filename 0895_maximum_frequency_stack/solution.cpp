// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

#include <algorithm>
#include <unordered_map>
#include <vector>

class FreqStack {
public:
    FreqStack() : maxfreq_(0) {}

    void push(int val) {
        int f = ++freq_[val];
        maxfreq_ = std::max(maxfreq_, f);
        group_[f].push_back(val);
    }

    int pop() {
        int val = group_[maxfreq_].back();
        group_[maxfreq_].pop_back();
        --freq_[val];
        if (group_[maxfreq_].empty()) {
            --maxfreq_;
        }
        return val;
    }

private:
    std::unordered_map<int, int> freq_;
    std::unordered_map<int, std::vector<int>> group_;
    int maxfreq_;
};
