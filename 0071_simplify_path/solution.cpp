// LeetCode 0071 - Simplify Path
// https://leetcode.com/problems/simplify-path/

#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::string simplifyPath(std::string path) {
        std::vector<std::string> stack;
        std::stringstream ss(path);
        std::string part;

        while (std::getline(ss, part, '/')) {
            if (part.empty() || part == ".") {
                continue;
            }
            if (part == "..") {
                if (!stack.empty()) {
                    stack.pop_back();
                }
            } else {
                stack.push_back(part);
            }
        }

        std::string result = "/";
        for (size_t i = 0; i < stack.size(); i++) {
            if (i > 0) {
                result += "/";
            }
            result += stack[i];
        }
        return result;
    }
};
