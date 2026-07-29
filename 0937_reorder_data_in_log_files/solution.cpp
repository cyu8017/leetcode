// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

#include <algorithm>
#include <cctype>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> reorderLogFiles(std::vector<std::string>& logs) {
        std::stable_sort(logs.begin(), logs.end(), [](const std::string& a, const std::string& b) {
            auto spa = a.find(' '), spb = b.find(' ');
            std::string resta = a.substr(spa + 1), restb = b.substr(spb + 1);
            bool letterA = std::isalpha(static_cast<unsigned char>(resta[0]));
            bool letterB = std::isalpha(static_cast<unsigned char>(restb[0]));
            if (letterA && letterB) {
                if (resta != restb) return resta < restb;
                return a.substr(0, spa) < b.substr(0, spb);
            }
            if (letterA != letterB) return letterA;
            return false;
        });
        return logs;
    }
};
