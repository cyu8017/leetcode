// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

#include <string>
#include <vector>

class Solution {
public:
    std::string addBoldTag(std::string s, std::vector<std::string>& words) {
        const int n = static_cast<int>(s.size());
        std::vector<bool> bold(n, false);
        for (const std::string& word : words) {
            std::size_t start = s.find(word);
            while (start != std::string::npos) {
                for (std::size_t i = start; i < start + word.size(); ++i) {
                    bold[i] = true;
                }
                start = s.find(word, start + 1);
            }
        }
        std::string parts;
        int i = 0;
        while (i < n) {
            if (bold[i]) {
                parts += "<b>";
                while (i < n && bold[i]) {
                    parts += s[i++];
                }
                parts += "</b>";
            } else {
                parts += s[i++];
            }
        }
        return parts;
    }
};
