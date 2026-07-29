// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

#include <condition_variable>
#include <functional>
#include <mutex>

class FizzBuzz {
private:
    int n;
    int current = 1;
    std::mutex mtx;
    std::condition_variable cv;

    void run(const std::function<bool(int)>& pred, const std::function<void()>& action) {
        while (true) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&] { return current > n || pred(current); });
            if (current > n) return;
            action();
            ++current;
            cv.notify_all();
        }
    }

public:
    FizzBuzz(int n) : n(n) {}

    void fizz(std::function<void()> printFizz) {
        run([](int x) { return x % 3 == 0 && x % 5 != 0; }, printFizz);
    }

    void buzz(std::function<void()> printBuzz) {
        run([](int x) { return x % 5 == 0 && x % 3 != 0; }, printBuzz);
    }

    void fizzbuzz(std::function<void()> printFizzBuzz) {
        run([](int x) { return x % 15 == 0; }, printFizzBuzz);
    }

    void number(std::function<void(int)> printNumber) {
        run([](int x) { return x % 3 != 0 && x % 5 != 0; },
            [&] { printNumber(current); });
    }
};
