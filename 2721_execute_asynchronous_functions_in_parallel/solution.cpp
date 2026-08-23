// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

#include <vector>
#include <functional>

class Solution {
public:
    // JS promiseAll stand-in: run sync functions in order
    std::vector<int> promiseAll(std::vector<std::function<int()>>& functions) {
        std::vector<int> out;
        for (auto& f : functions) out.push_back(f());
        return out;
    }
};
