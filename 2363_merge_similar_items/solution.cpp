// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

#include <map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> mergeSimilarItems(std::vector<std::vector<int>>& items1, std::vector<std::vector<int>>& items2) {
        std::map<int, int> mp;
        for (auto& it : items1) mp[it[0]] += it[1];
        for (auto& it : items2) mp[it[0]] += it[1];
        std::vector<std::vector<int>> ans;
        for (auto& [k, v] : mp) ans.push_back({k, v});
        return ans;
    }
};
