// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> splitWordsBySeparator(std::vector<std::string>& words, char separator) {
        std::vector<std::string> ans;
        for (auto& w : words) {
            int start = 0;
            for (int i = 0; i <= (int)w.size(); i++) {
                if (i == (int)w.size() || w[i] == separator) {
                    if (i > start) ans.push_back(w.substr(start, i - start));
                    start = i + 1;
                }
            }
        }
        return ans;
    }
};
