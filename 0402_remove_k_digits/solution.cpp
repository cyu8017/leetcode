// LeetCode 0402 - Remove K Digits
// https://leetcode.com/problems/remove-k-digits/

#include <string>
#include <vector>

class Solution {
public:
    string removeKdigits(string num, int k) {
        vector<char> stack;

        for (char digit : num) {
            while (k > 0 && !stack.empty() && stack.back() > digit) {
                stack.pop_back();
                --k;
            }
            stack.push_back(digit);
        }

        if (k > 0) {
            stack.resize(stack.size() - k);
        }

        int start = 0;
        while (start < static_cast<int>(stack.size()) - 1 && stack[start] == '0') {
            ++start;
        }

        string result(stack.begin() + start, stack.end());
        return result.empty() ? "0" : result;
    }
};
