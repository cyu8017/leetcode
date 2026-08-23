// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> fullJustify(std::vector<std::string>& words, int maxWidth) {
        std::vector<std::string> result;
        int i = 0;

        while (i < static_cast<int>(words.size())) {
            std::vector<std::string> lineWords;
            int lineLen = 0;

            while (i < static_cast<int>(words.size())) {
                const std::string& word = words[i];
                int extra = lineWords.empty() ? 0 : 1;
                if (lineLen + static_cast<int>(word.size()) + extra > maxWidth) {
                    break;
                }
                lineWords.push_back(word);
                lineLen += static_cast<int>(word.size()) + extra;
                i++;
            }

            if (i == static_cast<int>(words.size()) || lineWords.size() == 1) {
                std::string line;
                for (size_t j = 0; j < lineWords.size(); j++) {
                    if (j > 0) {
                        line += ' ';
                    }
                    line += lineWords[j];
                }
                line.append(static_cast<size_t>(maxWidth - static_cast<int>(line.size())), ' ');
                result.push_back(line);
            } else {
                int totalChars = 0;
                for (const std::string& word : lineWords) {
                    totalChars += static_cast<int>(word.size());
                }
                int totalSpaces = maxWidth - totalChars;
                int gaps = static_cast<int>(lineWords.size()) - 1;
                int space = totalSpaces / gaps;
                int remainder = totalSpaces % gaps;
                std::string line;
                for (int j = 0; j < static_cast<int>(lineWords.size()) - 1; j++) {
                    line += lineWords[j];
                    line.append(static_cast<size_t>(space + (j < remainder ? 1 : 0)), ' ');
                }
                line += lineWords.back();
                result.push_back(line);
            }
        }

        return result;
    }
};
