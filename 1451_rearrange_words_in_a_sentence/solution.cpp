#include <algorithm>
#include <cctype>
#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::string arrangeWords(std::string text) {
        for (char& c : text) c = (char)std::tolower(c);
        std::istringstream iss(text);
        std::vector<std::string> words;
        std::string w;
        while (iss >> w) words.push_back(w);
        std::stable_sort(words.begin(), words.end(), [](const std::string& a, const std::string& b) {
            return a.size() < b.size();
        });
        std::string answer;
        for (size_t i = 0; i < words.size(); ++i) {
            if (i) answer.push_back(' ');
            answer += words[i];
        }
        if (!answer.empty()) answer[0] = (char)std::toupper(answer[0]);
        return answer;
    }
};
