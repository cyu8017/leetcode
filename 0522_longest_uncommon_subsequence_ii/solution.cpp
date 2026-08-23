// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
    static bool isSubsequence(const std::string& target, const std::string& source) {
        size_t index = 0;
        for (const char ch : source) {
            if (index < target.size() && target[index] == ch) {
                ++index;
            }
        }
        return index == target.size();
    }

public:
    int findLUSlength(std::vector<std::string>& strs) {
        int result = -1;
        for (size_t i = 0; i < strs.size(); ++i) {
            bool uncommon = true;
            for (size_t j = 0; j < strs.size(); ++j) {
                if (i != j && isSubsequence(strs[i], strs[j])) {
                    uncommon = false;
                    break;
                }
            }
            if (uncommon) {
                result = std::max(result, static_cast<int>(strs[i].size()));
            }
        }
        return result;
    }
};
