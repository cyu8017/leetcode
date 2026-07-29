// LeetCode 1957 - Delete Characters to Make Fancy String
#include <string>

class Solution {
public:
    std::string makeFancyString(std::string s) {
        std::string ans;
        for (char c : s) {
            int n = (int)ans.size();
            if (n >= 2 && ans[n - 1] == c && ans[n - 2] == c) continue;
            ans.push_back(c);
        }
        return ans;
    }
};
