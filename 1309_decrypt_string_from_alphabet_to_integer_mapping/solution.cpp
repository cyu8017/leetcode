#include <algorithm>
#include <string>

class Solution {
public:
    std::string freqAlphabets(std::string s) {
        std::string answer;
        int i = (int)s.size() - 1;
        while (i >= 0) {
            if (s[i] == '#') {
                answer.push_back(char(96 + std::stoi(s.substr(i - 2, 2))));
                i -= 3;
            } else {
                answer.push_back(char(96 + (s[i] - '0')));
                --i;
            }
        }
        std::reverse(answer.begin(), answer.end());
        return answer;
    }
};
