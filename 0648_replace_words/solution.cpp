// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string replaceWords(std::vector<std::string>& dictionary, std::string sentence) {
        std::unordered_set<std::string> roots(dictionary.begin(), dictionary.end());
        std::stringstream ss(sentence);
        std::string word;
        std::string result;
        bool first = true;
        while (ss >> word) {
            std::string replacement = word;
            for (std::size_t i = 1; i <= word.size(); ++i) {
                const std::string prefix = word.substr(0, i);
                if (roots.count(prefix)) {
                    replacement = prefix;
                    break;
                }
            }
            if (!first) {
                result += ' ';
            }
            first = false;
            result += replacement;
        }
        return result;
    }
};
