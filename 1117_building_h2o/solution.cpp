// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

#include <condition_variable>
#include <functional>
#include <mutex>

class H2O {
public:
    H2O() : h(0), o(0) {}

    void hydrogen(std::function<void()> releaseHydrogen) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [this] { return h < 2; });
        ++h;
        releaseHydrogen();
        if (h == 2 && o == 1) {
            h = 0;
            o = 0;
        }
        cv.notify_all();
    }

    void oxygen(std::function<void()> releaseOxygen) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [this] { return o < 1; });
        ++o;
        releaseOxygen();
        if (h == 2 && o == 1) {
            h = 0;
            o = 0;
        }
        cv.notify_all();
    }

private:
    int h;
    int o;
    std::mutex mtx;
    std::condition_variable cv;
};
