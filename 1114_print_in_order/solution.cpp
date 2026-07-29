// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

#include <functional>
#include <mutex>

class Foo {
public:
    Foo() {
        m2.lock();
        m3.lock();
    }

    void first(std::function<void()> printFirst) {
        printFirst();
        m2.unlock();
    }

    void second(std::function<void()> printSecond) {
        m2.lock();
        printSecond();
        m3.unlock();
    }

    void third(std::function<void()> printThird) {
        m3.lock();
        printThird();
    }

private:
    std::mutex m2;
    std::mutex m3;
};
