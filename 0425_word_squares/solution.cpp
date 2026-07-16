// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

#include <algorithm>
#include <functional>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> wordSquares(std::vector<std::string>& words) {
        std::sort(words.begin(), words.end());
        int length = static_cast<int>(words[0].size());
        std::unordered_map<std::string, std::vector<std::string>> prefixMap;
        prefixMap[""] = words;

        for (const std::string& word : words) {
            for (int index = 0; index < length; ++index) {
                prefixMap[word.substr(0, index + 1)].push_back(word);
            }
        }

        std::vector<std::vector<std::string>> squares;
        std::vector<std::string> current;

        std::function<void(int)> dfs = [&](int row) {
            if (row == length) {
                squares.push_back(current);
                return;
            }

            std::string prefix;
            prefix.reserve(length);
            for (const std::string& word : current) {
                prefix.push_back(word[row]);
            }

            for (const std::string& candidate : prefixMap[prefix]) {
                current.push_back(candidate);
                dfs(row + 1);
                current.pop_back();
            }
        };

        dfs(0);
        return squares;
    }
};
