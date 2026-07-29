// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

#include <vector>

class MyCircularDeque {
    std::vector<int> data_;
    int capacity_;
    int front_ = 0;
    int size_ = 0;

public:
    MyCircularDeque(int k) : data_(k), capacity_(k) {}

    bool insertFront(int value) {
        if (isFull()) {
            return false;
        }
        front_ = (front_ - 1 + capacity_) % capacity_;
        data_[front_] = value;
        ++size_;
        return true;
    }

    bool insertLast(int value) {
        if (isFull()) {
            return false;
        }
        data_[(front_ + size_) % capacity_] = value;
        ++size_;
        return true;
    }

    bool deleteFront() {
        if (isEmpty()) {
            return false;
        }
        front_ = (front_ + 1) % capacity_;
        --size_;
        return true;
    }

    bool deleteLast() {
        if (isEmpty()) {
            return false;
        }
        --size_;
        return true;
    }

    int getFront() { return isEmpty() ? -1 : data_[front_]; }

    int getRear() {
        if (isEmpty()) {
            return -1;
        }
        return data_[(front_ + size_ - 1) % capacity_];
    }

    bool isEmpty() { return size_ == 0; }

    bool isFull() { return size_ == capacity_; }
};
