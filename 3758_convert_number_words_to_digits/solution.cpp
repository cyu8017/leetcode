// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

#include <string>
#include <vector>

class Solution {
public:
    std::string convertNumber(std::string s) {
        static const std::vector<std::string> d = {
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
        };
        int n = (int)s.size();
        std::string ans;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 10; j++) {
                int m = (int)d[j].size();
                if (i + m <= n && s.substr(i, m) == d[j]) {
                    ans.push_back(char('0' + j));
                    i += m - 1;
                    break;
                }
            }
        }
        return ans;
    }
};
