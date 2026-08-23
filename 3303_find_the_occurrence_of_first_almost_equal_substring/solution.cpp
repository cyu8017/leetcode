// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

#include <string>

class Solution {
public:
    int minStartingIndex(std::string s, std::string pattern) {
        int n = (int)s.size(), m = (int)pattern.size();
        for (int i = 0; i + m <= n; i++) {
            int diff = 0;
            for (int j = 0; j < m; j++) {
                if (s[i + j] != pattern[j]) {
                    diff++;
                    if (diff > 1) break;
                }
            }
            if (diff <= 1) return i;
        }
        return -1;
    }
};
