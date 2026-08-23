// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/
// JS-only problem; simplified string-map merge stand-in.

#include <string>
#include <unordered_map>

class Solution {
public:
    std::unordered_map<std::string, std::string> deepMerge(
        std::unordered_map<std::string, std::string>& obj1,
        std::unordered_map<std::string, std::string>& obj2) {
        std::unordered_map<std::string, std::string> out = obj1;
        for (auto& [k, v] : obj2) out[k] = v;
        return out;
    }
};
