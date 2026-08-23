// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

#include <map>
#include <string>
#include <vector>

class Solution {
public:
    // JS objDiff stand-in: keys where values differ
    std::map<std::string, std::vector<int>> objDiff(std::map<std::string, int>& obj1, std::map<std::string, int>& obj2) {
        std::map<std::string, std::vector<int>> diff;
        for (auto& [k, v] : obj1) {
            auto it = obj2.find(k);
            if (it != obj2.end() && it->second != v) diff[k] = {v, it->second};
        }
        return diff;
    }
};
