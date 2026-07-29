#include <algorithm>
#include <string>

class Solution {
public:
    int maxPower(std::string s) {
        int answer = 1, run = 1;
        for (size_t i = 1; i < s.size(); ++i) {
            run = s[i] == s[i - 1] ? run + 1 : 1;
            answer = std::max(answer, run);
        }
        return answer;
    }
};
