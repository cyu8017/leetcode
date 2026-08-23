// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool uniqueOccurrences(std::vector<int>& arr) {
        std::unordered_map<int, int> freq;
        for (int x : arr) {
            ++freq[x];
        }
        std::unordered_set<int> seen;
        for (const auto& [_, c] : freq) {
            if (!seen.insert(c).second) {
                return false;
            }
        }
        return true;
    }
};
