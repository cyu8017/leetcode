// LeetCode 1108 - Defanging an IP Address
// https://leetcode.com/problems/defanging-an-ip-address/

#include <string>

class Solution {
public:
    std::string defangIPaddr(std::string address) {
        std::string ans;
        for (char ch : address) {
            if (ch == '.') {
                ans += "[.]";
            } else {
                ans.push_back(ch);
            }
        }
        return ans;
    }
};
