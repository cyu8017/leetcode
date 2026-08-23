// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string shortestPalindrome(std::string s) {
        if (s.empty()) {
            return "";
        }
        std::string reversed = s;
        std::reverse(reversed.begin(), reversed.end());
        std::string combined = s + "#" + reversed;
        std::vector<int> pi(combined.size(), 0);
        int lps = 0;
        for (size_t i = 1; i < combined.size(); ++i) {
            while (lps > 0 && combined[i] != combined[lps]) {
                lps = pi[lps - 1];
            }
            if (combined[i] == combined[lps]) {
                lps += 1;
            }
            pi[i] = lps;
        }
        const int prefixLen = pi.back();
        return reversed.substr(0, s.size() - prefixLen) + s;
    }
};
