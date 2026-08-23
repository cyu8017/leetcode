// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

#include <string>
#include <unordered_map>

class MapSum {
    std::unordered_map<std::string, int> values_;
    std::unordered_map<std::string, int> prefixSums_;

public:
    MapSum() = default;

    void insert(std::string key, int val) {
        const int delta = val - (values_.count(key) ? values_[key] : 0);
        values_[key] = val;
        for (std::size_t i = 1; i <= key.size(); ++i) {
            prefixSums_[key.substr(0, i)] += delta;
        }
    }

    int sum(std::string prefix) {
        return prefixSums_.count(prefix) ? prefixSums_[prefix] : 0;
    }
};
