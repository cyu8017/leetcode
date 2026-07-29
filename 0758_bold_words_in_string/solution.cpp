// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

#include <string>
#include <vector>

class Solution {
public:
    std::string boldWords(std::vector<std::string>& words, std::string s) {
        int n = static_cast<int>(s.size());
        std::vector<bool> bold(n, false);
        for (const std::string& word : words) {
            size_t start = s.find(word);
            while (start != std::string::npos) {
                for (size_t i = start; i < start + word.size(); ++i) {
                    bold[i] = true;
                }
                start = s.find(word, start + 1);
            }
        }
        std::string parts;
        int i = 0;
        while (i < n) {
            if (bold[i]) {
                parts += "**";
                while (i < n && bold[i]) {
                    parts.push_back(s[i++]);
                }
                parts += "**";
            } else {
                parts.push_back(s[i++]);
            }
        }
        return parts;
    }
};
