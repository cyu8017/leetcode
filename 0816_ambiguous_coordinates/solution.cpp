// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> ambiguousCoordinates(std::string s) {
        std::string digits = s.substr(1, s.size() - 2);
        auto candidates = [](const std::string& frag) {
            std::vector<std::string> options;
            if (frag.empty() ||
                (frag.size() > 1 && frag.front() == '0' && frag.back() == '0')) {
                return options;
            }
            if (frag.front() == '0' && frag.size() > 1) {
                if (frag.back() != '0') {
                    options.push_back("0." + frag.substr(1));
                }
                return options;
            }
            options.push_back(frag);
            if (frag.back() == '0') {
                return options;
            }
            for (size_t i = 1; i < frag.size(); ++i) {
                options.push_back(frag.substr(0, i) + "." + frag.substr(i));
            }
            return options;
        };

        std::vector<std::string> answer;
        for (size_t i = 1; i < digits.size(); ++i) {
            for (const auto& left : candidates(digits.substr(0, i))) {
                for (const auto& right : candidates(digits.substr(i))) {
                    answer.push_back("(" + left + ", " + right + ")");
                }
            }
        }
        return answer;
    }
};
