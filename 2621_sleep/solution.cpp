// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

#include <chrono>
#include <thread>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    void sleep(int millis) {
        std::this_thread::sleep_for(std::chrono::milliseconds(millis));
    }
};
