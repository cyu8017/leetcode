#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> printVertically(std::string s) {
        std::istringstream iss(s);
        std::vector<std::string> words;
        std::string w;
        int maxLen = 0;
        while (iss >> w) {
            words.push_back(w);
            maxLen = std::max(maxLen, (int)w.size());
        }
        std::vector<std::string> answer;
        for (int i = 0; i < maxLen; ++i) {
            std::string row;
            for (auto& word : words) row.push_back(i < (int)word.size() ? word[i] : ' ');
            while (!row.empty() && row.back() == ' ') row.pop_back();
            answer.push_back(row);
        }
        return answer;
    }
};
