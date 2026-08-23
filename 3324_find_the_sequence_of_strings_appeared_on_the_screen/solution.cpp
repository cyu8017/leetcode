// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> stringSequence(std::string target) {
        std::vector<std::string> ans;
        std::string cur;
        for (char ch : target) {
            cur.push_back('a');
            ans.push_back(cur);
            while (cur.back() != ch) {
                cur.back()++;
                ans.push_back(cur);
            }
        }
        return ans;
    }
};
