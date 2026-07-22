// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

#include <deque>

class FrontMiddleBackQueue {
    std::deque<int> left_;
    std::deque<int> right_;

    void balance() {
        while (static_cast<int>(left_.size()) > static_cast<int>(right_.size()) + 1) {
            right_.push_front(left_.back());
            left_.pop_back();
        }
        while (static_cast<int>(right_.size()) > static_cast<int>(left_.size())) {
            left_.push_back(right_.front());
            right_.pop_front();
        }
    }

public:
    FrontMiddleBackQueue() {}

    void pushFront(int val) {
        left_.push_front(val);
        balance();
    }

    void pushMiddle(int val) {
        if (left_.size() > right_.size()) {
            right_.push_front(left_.back());
            left_.pop_back();
        }
        left_.push_back(val);
    }

    void pushBack(int val) {
        right_.push_back(val);
        balance();
    }

    int popFront() {
        if (left_.empty()) {
            return -1;
        }
        int v = left_.front();
        left_.pop_front();
        balance();
        return v;
    }

    int popMiddle() {
        if (left_.empty()) {
            return -1;
        }
        int v = left_.back();
        left_.pop_back();
        balance();
        return v;
    }

    int popBack() {
        if (left_.empty()) {
            return -1;
        }
        int v;
        if (!right_.empty()) {
            v = right_.back();
            right_.pop_back();
        } else {
            v = left_.back();
            left_.pop_back();
        }
        balance();
        return v;
    }
};
