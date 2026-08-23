// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> groups;

        for (const std::string& word : strs) {
            std::string key = word;
            std::sort(key.begin(), key.end());
            groups[key].push_back(word);
        }

        std::vector<std::vector<std::string>> result;
        result.reserve(groups.size());
        for (auto& entry : groups) {
            std::sort(entry.second.begin(), entry.second.end());
            result.push_back(std::move(entry.second));
        }
        auto minIndex = [&strs](const std::vector<std::string>& group) {
            int minIdx = static_cast<int>(strs.size());
            for (const std::string& word : group) {
                for (int i = 0; i < static_cast<int>(strs.size()); ++i) {
                    if (strs[i] == word) {
                        minIdx = std::min(minIdx, i);
                        break;
                    }
                }
            }
            return minIdx;
        };
        std::sort(result.begin(), result.end(), [&](const auto& a, const auto& b) {
            return minIndex(a) > minIndex(b);
        });
        return result;
    }
};
