// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> goodIndices(std::string s) {
        std::vector<int> ans;
        for (int i = 0; i < (int)s.size(); i++) {
            std::string t = std::to_string(i);
            int k = (int)t.size();
            if (i + 1 - k >= 0 && s.substr(i + 1 - k, k) == t) ans.push_back(i);
        }
        return ans;
    }
};
