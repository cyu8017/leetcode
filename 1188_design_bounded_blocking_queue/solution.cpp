// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

#include <condition_variable>
#include <mutex>
#include <queue>

class BoundedBlockingQueue {
public:
    BoundedBlockingQueue(int capacity) : capacity(capacity) {}

    void enqueue(int element) {
        std::unique_lock<std::mutex> lock(mtx);
        notFull.wait(lock, [&] { return static_cast<int>(q.size()) < capacity; });
        q.push(element);
        notEmpty.notify_one();
    }

    int dequeue() {
        std::unique_lock<std::mutex> lock(mtx);
        notEmpty.wait(lock, [&] { return !q.empty(); });
        int value = q.front();
        q.pop();
        notFull.notify_one();
        return value;
    }

    int size() {
        std::lock_guard<std::mutex> lock(mtx);
        return static_cast<int>(q.size());
    }

private:
    int capacity;
    std::queue<int> q;
    std::mutex mtx;
    std::condition_variable notFull;
    std::condition_variable notEmpty;
};
