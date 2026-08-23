// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> uncommonFromSentences(std::string s1, std::string s2) {
        std::unordered_map<std::string, int> count;
        auto add = [&](const std::string& s) {
            std::istringstream iss(s);
            std::string w;
            while (iss >> w) {
                ++count[w];
            }
        };
        add(s1);
        add(s2);
        std::vector<std::string> ans;
        for (auto& [w, c] : count) {
            if (c == 1) {
                ans.push_back(w);
            }
        }
        return ans;
    }
};
