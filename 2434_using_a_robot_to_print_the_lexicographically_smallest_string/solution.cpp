// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string robotWithString(std::string s) {
        int n = (int)s.size();
        std::vector<char> minSuf(n + 1);
        minSuf[n] = 'z' + 1;
        for (int i = n - 1; i >= 0; i--) {
            minSuf[i] = std::min(s[i], minSuf[i + 1]);
        }
        std::string stack, ans;
        for (int i = 0; i < n; i++) {
            stack.push_back(s[i]);
            while (!stack.empty() && stack.back() <= minSuf[i + 1]) {
                ans.push_back(stack.back());
                stack.pop_back();
            }
        }
        while (!stack.empty()) {
            ans.push_back(stack.back());
            stack.pop_back();
        }
        return ans;
    }
};
