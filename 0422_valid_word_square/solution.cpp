// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

#include <string>
#include <vector>

class Solution {
public:
    bool validWordSquare(std::vector<std::string>& words) {
        for (size_t row = 0; row < words.size(); ++row) {
            const std::string& word = words[row];
            for (size_t col = 0; col < word.size(); ++col) {
                if (col >= words.size() || row >= words[col].size() ||
                    words[col][row] != word[col]) {
                    return false;
                }
            }
        }
        return true;
    }
};
