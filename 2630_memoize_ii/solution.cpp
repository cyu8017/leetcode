// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

#include <functional>
#include <memory>
#include <string>
#include <unordered_map>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::function<int(const std::vector<int>&)> memoizeII(std::function<int(const std::vector<int>&)> fn) {
        auto cache = std::make_shared<std::unordered_map<std::string, int>>();
        return [fn, cache](const std::vector<int>& args) {
            std::string k;
            for (int a : args) k += "|" + std::to_string(a);
            auto it = cache->find(k);
            if (it != cache->end()) return it->second;
            int v = fn(args);
            (*cache)[k] = v;
            return v;
        };
    }
};
