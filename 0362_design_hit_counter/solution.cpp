// LeetCode 0362 - Design Hit Counter
// https://leetcode.com/problems/design-hit-counter/

#include <deque>

class HitCounter {
    std::deque<int> hits_;

public:
    HitCounter() {}

    void hit(int timestamp) {
        hits_.push_back(timestamp);
    }

    int getHits(int timestamp) {
        while (!hits_.empty() && hits_.front() <= timestamp - 300) {
            hits_.pop_front();
        }
        return static_cast<int>(hits_.size());
    }
};
