// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

#include <condition_variable>
#include <functional>
#include <mutex>

class ZeroEvenOdd {
public:
    ZeroEvenOdd(int n) : n(n), state(0) {}

    void zero(std::function<void(int)> printNumber) {
        for (int i = 1; i <= n; ++i) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [this] { return state == 0; });
            printNumber(0);
            state = (i % 2 == 1) ? 1 : 2;
            cv.notify_all();
        }
    }

    void even(std::function<void(int)> printNumber) {
        for (int num = 2; num <= n; num += 2) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [this] { return state == 2; });
            printNumber(num);
            state = 0;
            cv.notify_all();
        }
    }

    void odd(std::function<void(int)> printNumber) {
        for (int num = 1; num <= n; num += 2) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [this] { return state == 1; });
            printNumber(num);
            state = 0;
            cv.notify_all();
        }
    }

private:
    int n;
    int state;  // 0 = zero, 1 = odd, 2 = even
    std::mutex mtx;
    std::condition_variable cv;
};
