// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    std::string frequencySort(std::string s) {
        std::unordered_map<char, int> counts;
        for (char ch : s) {
            ++counts[ch];
        }

        std::vector<std::pair<char, int>> ordered(counts.begin(), counts.end());
        std::sort(ordered.begin(), ordered.end(), [](const auto& left, const auto& right) {
            if (left.second != right.second) {
                return left.second > right.second;
            }
            return left.first < right.first;
        });

        std::string result;
        for (const auto& [ch, count] : ordered) {
            result.append(count, ch);
        }
        return result;
    }
};
