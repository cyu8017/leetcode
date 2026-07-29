// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    std::string shortestCompletingWord(std::string licensePlate, std::vector<std::string>& words) {
        int need[26] = {};
        for (char ch : licensePlate) {
            if (std::isalpha(static_cast<unsigned char>(ch))) {
                ++need[std::tolower(static_cast<unsigned char>(ch)) - 'a'];
            }
        }
        std::string best;
        for (const std::string& word : words) {
            int counts[26] = {};
            for (char ch : word) {
                ++counts[ch - 'a'];
            }
            bool ok = true;
            for (int i = 0; i < 26; ++i) {
                if (counts[i] < need[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok && (best.empty() || word.size() < best.size())) {
                best = word;
            }
        }
        return best;
    }
};
