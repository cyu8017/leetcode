// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

#include <condition_variable>
#include <functional>
#include <mutex>

class FooBar {
public:
    FooBar(int n) : n(n), fooTurn(true) {}

    void foo(std::function<void()> printFoo) {
        for (int i = 0; i < n; ++i) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [this] { return fooTurn; });
            printFoo();
            fooTurn = false;
            cv.notify_all();
        }
    }

    void bar(std::function<void()> printBar) {
        for (int i = 0; i < n; ++i) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [this] { return !fooTurn; });
            printBar();
            fooTurn = true;
            cv.notify_all();
        }
    }

private:
    int n;
    bool fooTurn;
    std::mutex mtx;
    std::condition_variable cv;
};
