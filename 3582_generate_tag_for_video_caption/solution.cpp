// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

#include <cctype>
#include <sstream>
#include <string>

class Solution {
public:
    std::string generateTag(std::string caption) {
        std::istringstream iss(caption);
        std::string word, ans = "#";
        int i = 0;
        while (iss >> word) {
            for (char& c : word) c = (char)std::tolower((unsigned char)c);
            if (i == 0) ans += word;
            else {
                if (!word.empty()) word[0] = (char)std::toupper((unsigned char)word[0]);
                ans += word;
            }
            if ((int)ans.size() >= 100) break;
            i++;
        }
        if ((int)ans.size() > 100) ans.resize(100);
        return ans;
    }
};
