// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

#include <vector>

class MyCircularQueue {
    std::vector<int> data_;
    int capacity_;
    int head_ = 0;
    int size_ = 0;

public:
    MyCircularQueue(int k) : data_(k), capacity_(k) {}

    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }
        data_[(head_ + size_) % capacity_] = value;
        ++size_;
        return true;
    }

    bool deQueue() {
        if (isEmpty()) {
            return false;
        }
        head_ = (head_ + 1) % capacity_;
        --size_;
        return true;
    }

    int Front() { return isEmpty() ? -1 : data_[head_]; }

    int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return data_[(head_ + size_ - 1) % capacity_];
    }

    bool isEmpty() { return size_ == 0; }

    bool isFull() { return size_ == capacity_; }
};
