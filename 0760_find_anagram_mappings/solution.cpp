// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> anagramMappings(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_map<int, std::queue<int>> positions;
        for (int i = 0; i < static_cast<int>(nums2.size()); ++i) {
            positions[nums2[i]].push(i);
        }
        std::vector<int> result;
        result.reserve(nums1.size());
        for (int value : nums1) {
            result.push_back(positions[value].front());
            positions[value].pop();
        }
        return result;
    }
};
