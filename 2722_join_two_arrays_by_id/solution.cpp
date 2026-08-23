// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

#include <vector>
#include <map>
#include <string>
#include <algorithm>

class Solution {
public:
    // JS join-by-id stand-in for maps with int id
    std::vector<std::map<std::string, int>> join(
        std::vector<std::map<std::string, int>>& arr1,
        std::vector<std::map<std::string, int>>& arr2) {
        std::map<int, std::map<std::string, int>> byId;
        auto merge = [&](std::vector<std::map<std::string, int>>& arr) {
            for (auto& obj : arr) {
                int id = obj.at("id");
                auto& dest = byId[id];
                for (auto& [k, v] : obj) dest[k] = v;
            }
        };
        merge(arr1); merge(arr2);
        std::vector<std::map<std::string, int>> out;
        for (auto& [_, obj] : byId) out.push_back(obj);
        return out;
    }
};
