// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

#include <map>
#include <string>
#include <vector>
#include <functional>

class Solution {
public:
    // JS immutability helper stand-in
    std::vector<std::map<std::string, int>> immutableHelper(
        std::map<std::string, int> obj,
        std::vector<std::function<void(std::map<std::string, int>&)>> mutators) {
        std::vector<std::map<std::string, int>> out;
        for (auto& m : mutators) {
            auto copy = obj;
            m(copy);
            out.push_back(copy);
        }
        return out;
    }
};
