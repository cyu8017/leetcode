// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool differByOne(std::vector<std::string>& dict) {
        std::unordered_set<std::string> seen;
        for (const std::string& word : dict) {
            for (std::size_t i = 0; i < word.size(); ++i) {
                std::string pattern = word;
                pattern[i] = '*';
                if (seen.count(pattern)) {
                    return true;
                }
                seen.insert(pattern);
            }
        }
        return false;
    }
};
