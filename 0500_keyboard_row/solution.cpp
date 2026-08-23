// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

#include <cctype>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
    static bool onOneRow(const std::string& word) {
        static const std::unordered_set<char> rows[3] = {
            {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
            {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm'},
        };
        std::unordered_set<char> letters;
        for (char ch : word) {
            if (std::isalpha(static_cast<unsigned char>(ch))) {
                letters.insert(static_cast<char>(std::tolower(static_cast<unsigned char>(ch))));
            }
        }
        for (const auto& row : rows) {
            bool subset = true;
            for (char ch : letters) {
                if (row.count(ch) == 0) {
                    subset = false;
                    break;
                }
            }
            if (subset) {
                return true;
            }
        }
        return false;
    }

public:
    std::vector<std::string> findWords(std::vector<std::string>& words) {
        std::vector<std::string> result;
        for (const auto& word : words) {
            if (onOneRow(word)) {
                result.push_back(word);
            }
        }
        return result;
    }
};
