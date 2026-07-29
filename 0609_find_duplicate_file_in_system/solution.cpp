// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> findDuplicate(std::vector<std::string>& paths) {
        std::unordered_map<std::string, std::vector<std::string>> contentToPaths;
        for (const std::string& entry : paths) {
            std::stringstream ss(entry);
            std::string directory;
            ss >> directory;
            std::string fileInfo;
            while (ss >> fileInfo) {
                const auto open = fileInfo.find('(');
                const std::string name = fileInfo.substr(0, open);
                const std::string content = fileInfo.substr(open + 1, fileInfo.size() - open - 2);
                contentToPaths[content].push_back(directory + "/" + name);
            }
        }
        std::vector<std::vector<std::string>> result;
        for (auto& [_, group] : contentToPaths) {
            if (group.size() > 1) {
                result.push_back(std::move(group));
            }
        }
        return result;
    }
};
