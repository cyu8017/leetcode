// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

#include <string>
#include <vector>

class Solution {
public:
    std::string minRemoveToMakeValid(std::string s) {
        std::vector<int> opens;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            if (s[i] == '(') {
                opens.push_back(i);
            } else if (s[i] == ')') {
                if (!opens.empty()) {
                    opens.pop_back();
                } else {
                    s[i] = '*';
                }
            }
        }
        for (int i : opens) {
            s[i] = '*';
        }
        std::string answer;
        for (char ch : s) {
            if (ch != '*') {
                answer.push_back(ch);
            }
        }
        return answer;
    }
};
