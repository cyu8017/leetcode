// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> removeSubfolders(std::vector<std::string>& folder) {
        std::sort(folder.begin(), folder.end());
        std::vector<std::string> answer;
        for (const std::string& path : folder) {
            if (answer.empty() || path.compare(0, answer.back().size() + 1, answer.back() + "/") != 0) {
                answer.push_back(path);
            }
        }
        return answer;
    }
};
