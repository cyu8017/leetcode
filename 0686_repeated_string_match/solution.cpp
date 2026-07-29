// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

#include <string>

class Solution {
public:
    int repeatedStringMatch(std::string a, std::string b) {
        const int repeats = static_cast<int>((b.size() + a.size() - 1) / a.size());
        std::string built;
        built.reserve(a.size() * (repeats + 1));
        for (int i = 0; i < repeats; ++i) {
            built += a;
        }
        if (built.find(b) != std::string::npos) {
            return repeats;
        }
        built += a;
        if (built.find(b) != std::string::npos) {
            return repeats + 1;
        }
        return -1;
    }
};
