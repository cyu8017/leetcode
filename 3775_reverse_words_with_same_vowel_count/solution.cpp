// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

class Solution {
    static int calc(const std::string& w) {
        int cnt = 0;
        for (char c : w) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt++;
        }
        return cnt;
    }

public:
    std::string reverseWords(std::string s) {
        std::istringstream iss(s);
        std::vector<std::string> words;
        std::string w;
        while (iss >> w) words.push_back(w);

        int cnt = calc(words[0]);
        std::vector<std::string> ans;
        ans.push_back(words[0]);

        for (int i = 1; i < (int)words.size(); i++) {
            w = words[i];
            if (calc(w) == cnt) std::reverse(w.begin(), w.end());
            ans.push_back(w);
        }

        std::ostringstream oss;
        for (int i = 0; i < (int)ans.size(); i++) {
            if (i) oss << ' ';
            oss << ans[i];
        }
        return oss.str();
    }
};
