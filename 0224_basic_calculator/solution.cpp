// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> st;
        int result = 0;
        int number = 0;
        int sign = 1;
        for (char ch : s) {
            if (isdigit(ch)) {
                number = number * 10 + (ch - '0');
            } else if (ch == '+' || ch == '-') {
                result += sign * number;
                number = 0;
                sign = ch == '+' ? 1 : -1;
            } else if (ch == '(') {
                st.push(result);
                st.push(sign);
                result = 0;
                sign = 1;
            } else if (ch == ')') {
                result += sign * number;
                number = 0;
                result *= st.top();
                st.pop();
                result += st.top();
                st.pop();
            }
        }
        result += sign * number;
        return result;
    }
};
