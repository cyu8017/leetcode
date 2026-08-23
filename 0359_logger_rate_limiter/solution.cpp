// LeetCode 0359 - Logger Rate Limiter
// https://leetcode.com/problems/logger-rate-limiter/

#include <string>
#include <unordered_map>

class Logger {
    std::unordered_map<std::string, int> lastPrinted_;

public:
    Logger() {}

    bool shouldPrintMessage(int timestamp, std::string message) {
        auto iterator = lastPrinted_.find(message);
        if (iterator == lastPrinted_.end() || timestamp - iterator->second >= 10) {
            lastPrinted_[message] = timestamp;
            return true;
        }
        return false;
    }
};
