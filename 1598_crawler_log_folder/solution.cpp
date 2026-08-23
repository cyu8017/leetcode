// LeetCode 1598 - Crawler Log Folder
// https://leetcode.com/problems/crawler-log-folder/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<std::string>& logs) {
        int depth = 0;
        for (const auto& log : logs) {
            if (log == "../") {
                depth = std::max(0, depth - 1);
            } else if (log != "./") {
                ++depth;
            }
        }
        return depth;
    }
};
