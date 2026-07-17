// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

#include <string>
#include <utility>

class Solution {
public:
    int maximumGain(std::string s, int x, int y) {
        int first;
        int second;
        if (x >= y) {
            auto [rest, gainedFirst] = remove(s, 'a', 'b', x);
            first = gainedFirst;
            second = remove(rest, 'b', 'a', y).second;
        } else {
            auto [rest, gainedFirst] = remove(s, 'b', 'a', y);
            first = gainedFirst;
            second = remove(rest, 'a', 'b', x).second;
        }
        return first + second;
    }

private:
    std::pair<std::string, int> remove(const std::string& text, char open, char close, int score) {
        std::string stack;
        int gained = 0;
        for (char ch : text) {
            if (!stack.empty() && stack.back() == open && ch == close) {
                stack.pop_back();
                gained += score;
            } else {
                stack.push_back(ch);
            }
        }
        return { stack, gained };
    }
};
