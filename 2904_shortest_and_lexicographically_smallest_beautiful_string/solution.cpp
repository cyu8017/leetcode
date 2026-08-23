// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

#include <string>

class Solution {
public:
    std::string shortestBeautifulSubstring(std::string s, int k) {
        std::string ans;
        int n = (int)s.size();
        for (int i = 0; i < n; i++) {
            int ones = 0;
            for (int j = i; j < n; j++) {
                if (s[j] == '1') ones++;
                if (ones == k) {
                    std::string cand = s.substr(i, j - i + 1);
                    if (ans.empty() || cand.size() < ans.size() || (cand.size() == ans.size() && cand < ans))
                        ans = cand;
                    break;
                }
                if (ones > k) break;
            }
        }
        return ans;
    }
};
