// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> scoreValidator(std::vector<std::string>& events) {
        int score = 0, counter = 0;
        for (auto& event : events) {
            bool isNum = !event.empty();
            int num = 0;
            int start = 0;
            if (isNum && event[0] == '-') start = 1;
            for (int i = start; i < (int)event.size(); i++) {
                if (event[i] < '0' || event[i] > '9') {
                    isNum = false;
                    break;
                }
                num = num * 10 + (event[i] - '0');
            }
            if (isNum && !(start == 1 && event.size() == 1)) {
                if (start == 1) num = -num;
                score += num;
            } else if (event == "W") {
                counter++;
                if (counter == 10) break;
            } else {
                score++;
            }
        }
        return {score, counter};
    }
};
