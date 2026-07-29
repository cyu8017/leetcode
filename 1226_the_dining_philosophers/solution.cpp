// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

#include <functional>
#include <mutex>

class DiningPhilosophers {
public:
    DiningPhilosophers() = default;

    void wantsToEat(int philosopher,
                    std::function<void()> pickLeftFork,
                    std::function<void()> pickRightFork,
                    std::function<void()> eat,
                    std::function<void()> putLeftFork,
                    std::function<void()> putRightFork) {
        int left = philosopher;
        int right = (philosopher + 1) % 5;
        int first = philosopher % 2 == 0 ? left : right;
        int second = philosopher % 2 == 0 ? right : left;
        std::scoped_lock lock(forks[first], forks[second]);
        pickLeftFork();
        pickRightFork();
        eat();
        putLeftFork();
        putRightFork();
    }

private:
    std::mutex forks[5];
};
