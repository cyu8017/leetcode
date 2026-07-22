// LeetCode 1678 - Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

#include <string>

class Solution {
public:
    std::string interpret(std::string command) {
        std::string out;
        for (size_t i = 0; i < command.size();) {
            if (command[i] == 'G') {
                out.push_back('G');
                ++i;
            } else if (command[i] == '(' && command[i + 1] == ')') {
                out.push_back('o');
                i += 2;
            } else {
                out += "al";
                i += 4;
            }
        }
        return out;
    }
};
