// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

class LogSystem {
    std::vector<std::pair<int, std::string>> logs_;
    std::unordered_map<std::string, int> granularityIndex_ = {
        {"Year", 4},
        {"Month", 7},
        {"Day", 10},
        {"Hour", 13},
        {"Minute", 16},
        {"Second", 19},
    };

public:
    LogSystem() = default;

    void put(int id, std::string timestamp) { logs_.emplace_back(id, timestamp); }

    std::vector<int> retrieve(std::string start, std::string end, std::string granularity) {
        const int index = granularityIndex_[granularity];
        const std::string startKey = start.substr(0, index);
        const std::string endKey = end.substr(0, index);
        std::vector<std::pair<std::string, int>> matched;
        for (const auto& [logId, timestamp] : logs_) {
            const std::string key = timestamp.substr(0, index);
            if (startKey <= key && key <= endKey) {
                matched.emplace_back(timestamp, logId);
            }
        }
        std::sort(matched.begin(), matched.end());
        std::vector<int> result;
        for (const auto& [_, logId] : matched) {
            result.push_back(logId);
        }
        return result;
    }
};
