// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

#include <string>
#include <vector>

class Solution {
public:
    std::string oddString(std::vector<std::string>& words) {
        auto diff = [](const std::string& w) {
            std::string b;
            for (int i = 1; i < (int)w.size(); i++) {
                int d = (int)w[i] - (int)w[i - 1];
                b.push_back((char)(d + 128));
                b.push_back(',');
            }
            return b;
        };
        std::string d0 = diff(words[0]), d1 = diff(words[1]);
        if (d0 == d1) {
            for (int i = 2; i < (int)words.size(); i++) {
                if (diff(words[i]) != d0) return words[i];
            }
        }
        if (diff(words[2]) == d0) return words[1];
        return words[0];
    }
};
