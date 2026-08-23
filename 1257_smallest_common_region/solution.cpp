// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string findSmallestRegion(std::vector<std::vector<std::string>>& regions, std::string region1,
                                   std::string region2) {
        std::unordered_map<std::string, std::string> parent;
        for (const auto& group : regions) {
            for (int i = 1; i < static_cast<int>(group.size()); ++i) {
                parent[group[i]] = group[0];
            }
        }
        std::unordered_set<std::string> ancestors;
        while (!region1.empty()) {
            ancestors.insert(region1);
            auto it = parent.find(region1);
            if (it == parent.end()) {
                break;
            }
            region1 = it->second;
        }
        while (!ancestors.count(region2)) {
            region2 = parent[region2];
        }
        return region2;
    }
};
