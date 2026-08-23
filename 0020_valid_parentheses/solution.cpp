// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

#include <stack>
#include <string>
#include <unordered_map>

class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> st;
        std::unordered_map<char, char> pairs = {
            {')', '('},
            {']', '['},
            {'}', '{'},
        };

        for (char ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                st.push(ch);
            } else if (st.empty() || st.top() != pairs[ch]) {
                return false;
            } else {
                st.pop();
            }
        }

        return st.empty();
    }
};
