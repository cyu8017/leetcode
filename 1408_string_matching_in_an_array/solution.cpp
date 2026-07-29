#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> stringMatching(std::vector<std::string>& words) {
        std::vector<std::string> answer;
        for (size_t i = 0; i < words.size(); ++i) {
            for (size_t j = 0; j < words.size(); ++j) {
                if (i != j && words[j].find(words[i]) != std::string::npos) {
                    answer.push_back(words[i]);
                    break;
                }
            }
        }
        return answer;
    }
};
