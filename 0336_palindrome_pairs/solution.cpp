// LeetCode 0336 - Palindrome Pairs
// https://leetcode.com/problems/palindrome-pairs/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> palindromePairs(std::vector<std::string>& words) {
        std::unordered_map<std::string, int> wordMap;
        for (int index = 0; index < static_cast<int>(words.size()); index++) {
            wordMap[words[index]] = index;
        }

        std::unordered_set<long long> seen;
        auto pairKey = [](int left, int right) {
            return (static_cast<long long>(left) << 32) |
                static_cast<unsigned int>(right);
        };

        for (int index = 0; index < static_cast<int>(words.size()); index++) {
            const std::string& word = words[index];
            for (int split = 0; split <= static_cast<int>(word.size()); split++) {
                std::string left = word.substr(0, split);
                std::string right = word.substr(split);
                if (isPalindrome(left)) {
                    std::string reversedRight(right.rbegin(), right.rend());
                    auto iterator = wordMap.find(reversedRight);
                    if (iterator != wordMap.end() && iterator->second != index) {
                        seen.insert(pairKey(iterator->second, index));
                    }
                }
                if (isPalindrome(right)) {
                    std::string reversedLeft(left.rbegin(), left.rend());
                    auto iterator = wordMap.find(reversedLeft);
                    if (iterator != wordMap.end() && iterator->second != index) {
                        seen.insert(pairKey(index, iterator->second));
                    }
                }
            }
        }

        std::vector<std::vector<int>> result;
        result.reserve(seen.size());
        for (long long key : seen) {
            result.push_back({
                static_cast<int>(key >> 32),
                static_cast<int>(key & 0xffffffff),
            });
        }
        return result;
    }

private:
    static bool isPalindrome(const std::string& value) {
        int left = 0;
        int right = static_cast<int>(value.size()) - 1;
        while (left < right) {
            if (value[left] != value[right]) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
};
