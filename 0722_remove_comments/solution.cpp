// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> removeComments(std::vector<std::string>& source) {
        std::vector<std::string> result;
        std::string buffer;
        bool inBlock = false;
        for (const std::string& line : source) {
            size_t i = 0;
            while (i < line.size()) {
                if (inBlock) {
                    if (i + 1 < line.size() && line[i] == '*' && line[i + 1] == '/') {
                        inBlock = false;
                        i += 2;
                    } else {
                        ++i;
                    }
                } else if (i + 1 < line.size() && line[i] == '/' && line[i + 1] == '*') {
                    inBlock = true;
                    i += 2;
                } else if (i + 1 < line.size() && line[i] == '/' && line[i + 1] == '/') {
                    break;
                } else {
                    buffer.push_back(line[i++]);
                }
            }
            if (!inBlock && !buffer.empty()) {
                result.push_back(buffer);
                buffer.clear();
            }
        }
        return result;
    }
};
