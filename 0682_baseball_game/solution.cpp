// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

#include <string>
#include <vector>

class Solution {
public:
    int calPoints(std::vector<std::string>& operations) {
        std::vector<int> stack;
        for (const std::string& op : operations) {
            if (op == "C") {
                stack.pop_back();
            } else if (op == "D") {
                stack.push_back(stack.back() * 2);
            } else if (op == "+") {
                stack.push_back(stack.back() + stack[stack.size() - 2]);
            } else {
                stack.push_back(std::stoi(op));
            }
        }
        int total = 0;
        for (int value : stack) {
            total += value;
        }
        return total;
    }
};
