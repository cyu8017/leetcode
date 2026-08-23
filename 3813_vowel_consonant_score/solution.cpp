// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

#include <cctype>
#include <string>

class Solution {
public:
    int vowelConsonantScore(std::string s) {
        int v = 0, c = 0;
        for (char ch : s) {
            if (std::isalpha(static_cast<unsigned char>(ch))) {
                c++;
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') v++;
            }
        }
        c -= v;
        if (c == 0) return 0;
        return v / c;
    }
};
