// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

class TimeMap {
public:
    TimeMap() {}

    void set(std::string key, std::string value, int timestamp) {
        store[key].emplace_back(timestamp, value);
    }

    std::string get(std::string key, int timestamp) {
        auto it = store.find(key);
        if (it == store.end()) return "";
        auto& arr = it->second;
        auto pos = std::upper_bound(arr.begin(), arr.end(), timestamp,
            [](int t, const std::pair<int, std::string>& p) { return t < p.first; });
        if (pos == arr.begin()) return "";
        return std::prev(pos)->second;
    }

private:
    std::unordered_map<std::string, std::vector<std::pair<int, std::string>>> store;
};
