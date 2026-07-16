// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

#include <deque>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
    static bool isValid(const std::string& text) {
        int balance = 0;
        for (char character : text) {
            if (character == '(') {
                balance += 1;
            } else if (character == ')') {
                if (balance == 0) {
                    return false;
                }
                balance -= 1;
            }
        }
        return balance == 0;
    }

public:
    std::vector<std::string> removeInvalidParentheses(std::string s) {
        std::unordered_set<std::string> result;
        std::deque<std::string> queue;
        std::unordered_set<std::string> visited;
        queue.push_back(s);
        visited.insert(s);
        bool found = false;

        while (!queue.empty()) {
            int levelSize = static_cast<int>(queue.size());
            for (int level = 0; level < levelSize; level++) {
                std::string current = queue.front();
                queue.pop_front();
                if (isValid(current)) {
                    result.insert(current);
                    found = true;
                }
                if (found) {
                    continue;
                }
                for (size_t index = 0; index < current.size(); index++) {
                    if (current[index] != '(' && current[index] != ')') {
                        continue;
                    }
                    std::string next = current.substr(0, index) + current.substr(index + 1);
                    if (visited.insert(next).second) {
                        queue.push_back(next);
                    }
                }
            }
        }

        return std::vector<std::string>(result.begin(), result.end());
    }
};
