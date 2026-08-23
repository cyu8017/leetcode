// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    bool buddyStrings(std::string s, std::string goal) {
        if (s.size() != goal.size()) {
            return false;
        }
        if (s == goal) {
            return std::unordered_set<char>(s.begin(), s.end()).size() < s.size();
        }
        std::vector<std::pair<char, char>> diffs;
        for (size_t i = 0; i < s.size(); ++i) {
            if (s[i] != goal[i]) {
                diffs.emplace_back(s[i], goal[i]);
            }
        }
        return diffs.size() == 2 && diffs[0].first == diffs[1].second &&
               diffs[0].second == diffs[1].first;
    }
};
