// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

#include <algorithm>
#include <string>
#include <unordered_set>

class Solution {
public:
    int maxUniqueSplit(std::string s) {
        std::unordered_set<std::string> used;
        int answer = 0;
        dfs(s, 0, used, answer);
        return answer;
    }

private:
    void dfs(const std::string& s, int i, std::unordered_set<std::string>& used, int& answer) {
        if (static_cast<int>(used.size()) + static_cast<int>(s.size()) - i <= answer) {
            return;
        }
        if (i == static_cast<int>(s.size())) {
            answer = std::max(answer, static_cast<int>(used.size()));
            return;
        }
        for (int j = i + 1; j <= static_cast<int>(s.size()); ++j) {
            std::string part = s.substr(i, j - i);
            if (!used.count(part)) {
                used.insert(part);
                dfs(s, j, used, answer);
                used.erase(part);
            }
        }
    }
};
