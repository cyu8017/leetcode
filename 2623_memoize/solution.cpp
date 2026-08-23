// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

#include <functional>
#include <memory>
#include <unordered_map>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::function<int(int)> memoize(std::function<int(int)> fn) {
        auto cache = std::make_shared<std::unordered_map<int, int>>();
        return [fn, cache](int x) {
            auto it = cache->find(x);
            if (it != cache->end()) return it->second;
            int v = fn(x);
            (*cache)[x] = v;
            return v;
        };
    }
};
