// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/
// JS-only problem; C++ string-map stand-in.

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::unordered_map<std::string, std::vector<std::string>> invertObject(
        std::unordered_map<std::string, std::string>& obj) {
        std::unordered_map<std::string, std::vector<std::string>> out;
        for (auto& [k, v] : obj) out[v].push_back(k);
        return out;
    }
};
