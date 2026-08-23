// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

#include <unordered_map>
#include <vector>
#include <string>
#include <functional>

// JS EventEmitter stand-in
class EventEmitter {
    std::unordered_map<std::string, std::vector<std::function<void(const std::vector<int>&)>>> handlers;
public:
    EventEmitter() {}
    std::function<void()> subscribe(std::string eventName, std::function<void(const std::vector<int>&)> callback) {
        handlers[eventName].push_back(callback);
        int idx = (int)handlers[eventName].size() - 1;
        return [this, eventName, idx]() mutable {
            auto& v = handlers[eventName];
            if (idx >= 0 && idx < (int)v.size()) {
                v.erase(v.begin() + idx);
                idx = -1;
            }
        };
    }
    std::vector<int> emit(std::string eventName, std::vector<int> args) {
        std::vector<int> res;
        for (auto& cb : handlers[eventName]) {
            cb(args);
            res.push_back(0);
        }
        return res;
    }
};

class Solution {
public:
    EventEmitter createEmitter() { return EventEmitter(); }
};
