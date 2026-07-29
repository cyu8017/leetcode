#include <cctype>
#include <cmath>
#include <string>

class Solution {
public:
    std::string reformat(std::string s) {
        std::string letters, digits;
        for (char c : s) {
            if (std::isalpha((unsigned char)c)) letters.push_back(c);
            else digits.push_back(c);
        }
        if (std::abs((int)letters.size() - (int)digits.size()) > 1) return "";
        if (digits.size() > letters.size()) std::swap(letters, digits);
        std::string answer;
        for (size_t i = 0; i < letters.size(); ++i) {
            answer.push_back(letters[i]);
            if (i < digits.size()) answer.push_back(digits[i]);
        }
        return answer;
    }
};
