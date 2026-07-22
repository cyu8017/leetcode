// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

#include <string>
#include <vector>

class Solution {
public:
    std::string reformatNumber(std::string number) {
        std::string s;
        for (char c : number) {
            if (c >= '0' && c <= '9') {
                s.push_back(c);
            }
        }
        std::vector<std::string> out;
        while (static_cast<int>(s.size()) > 4) {
            out.push_back(s.substr(0, 3));
            s = s.substr(3);
        }
        if (s.size() == 4) {
            out.push_back(s.substr(0, 2));
            out.push_back(s.substr(2));
        } else if (!s.empty()) {
            out.push_back(s);
        }
        std::string ans = out[0];
        for (size_t i = 1; i < out.size(); ++i) {
            ans += "-" + out[i];
        }
        return ans;
    }
};
