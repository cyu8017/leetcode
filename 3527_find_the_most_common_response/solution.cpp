// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    std::string findCommonResponse(std::vector<std::vector<std::string>>& responses) {
        std::unordered_map<std::string, int> cnt;
        for (auto& ws : responses) {
            std::unordered_set<std::string> s;
            for (auto& w : ws) {
                if (s.insert(w).second) cnt[w]++;
            }
        }
        std::string ans = responses[0][0];
        for (auto& [w, v] : cnt) {
            if (cnt[ans] < v || (cnt[ans] == v && w < ans)) ans = w;
        }
        return ans;
    }
};
