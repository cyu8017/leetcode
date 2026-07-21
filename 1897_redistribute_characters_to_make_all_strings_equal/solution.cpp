// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

#include <string>
#include <vector>

class Solution {
public:
    bool makeEqual(std::vector<std::string>& words) {
        std::vector<int> counts(26, 0);
        for (const std::string& word : words) {
            for (char ch : word) {
                counts[ch - 'a']++;
            }
        }
        int n = static_cast<int>(words.size());
        for (int total : counts) {
            if (total % n != 0) {
                return false;
            }
        }
        return true;
    }
};
