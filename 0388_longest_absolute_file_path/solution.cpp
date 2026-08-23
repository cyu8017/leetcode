// LeetCode 0388 - Longest Absolute File Path
// https://leetcode.com/problems/longest-absolute-file-path/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int lengthLongestPath(std::string input) {
        std::vector<int> stack;
        int maxLength = 0;
        int index = 0;

        while (index < static_cast<int>(input.size())) {
            int end = index;
            while (end < static_cast<int>(input.size()) && input[end] != '\n') {
                end += 1;
            }

            std::string line = input.substr(index, end - index);
            int depth = 0;
            while (depth < static_cast<int>(line.size()) && line[depth] == '\t') {
                depth += 1;
            }
            std::string name = line.substr(depth);

            while (static_cast<int>(stack.size()) > depth) {
                stack.pop_back();
            }

            if (name.find('.') != std::string::npos) {
                int prefix = stack.empty() ? 0 : stack.back();
                maxLength = std::max(maxLength, prefix + static_cast<int>(name.size()));
            } else {
                int prefix = stack.empty() ? 0 : stack.back();
                stack.push_back(prefix + static_cast<int>(name.size()) + 1);
            }

            index = end + 1;
        }

        return maxLength;
    }
};
