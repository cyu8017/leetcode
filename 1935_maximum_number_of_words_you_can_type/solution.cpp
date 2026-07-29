// LeetCode 1935 - Maximum Number of Words You Can Type
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

#include <sstream>
#include <string>
#include <unordered_set>

class Solution {
public:
    int canBeTypedWords(std::string text, std::string brokenLetters) {
        std::unordered_set<char> broken(brokenLetters.begin(), brokenLetters.end());
        std::istringstream iss(text);
        std::string w;
        int ans = 0;
        while (iss >> w) {
            bool ok = true;
            for (char c : w) if (broken.count(c)) { ok = false; break; }
            if (ok) ans++;
        }
        return ans;
    }
};
