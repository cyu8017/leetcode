// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool reportSpam(std::vector<std::string>& message, std::vector<std::string>& bannedWords) {
        std::unordered_set<std::string> ban(bannedWords.begin(), bannedWords.end());
        int cnt = 0;
        for (auto& w : message) {
            if (ban.count(w)) {
                cnt++;
                if (cnt >= 2) return true;
            }
        }
        return false;
    }
};
