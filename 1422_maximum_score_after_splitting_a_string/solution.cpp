#include <algorithm>
#include <string>

class Solution {
public:
    int maxScore(std::string s) {
        int ones = 0;
        for (char c : s) ones += c == '1';
        int leftZeros = 0, answer = 0;
        for (size_t i = 0; i + 1 < s.size(); ++i) {
            if (s[i] == '0') ++leftZeros;
            else --ones;
            answer = std::max(answer, leftZeros + ones);
        }
        return answer;
    }
};
