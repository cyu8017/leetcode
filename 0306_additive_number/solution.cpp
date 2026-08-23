// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

#include <string>

class Solution {
    bool valid(const std::string& num, std::string first, std::string second, int start) {
        if ((first.size() > 1 && first[0] == '0') || (second.size() > 1 && second[0] == '0')) {
            return false;
        }
        while (start < static_cast<int>(num.size())) {
            long long total = std::stoll(first) + std::stoll(second);
            std::string totalText = std::to_string(total);
            if (num.compare(start, totalText.size(), totalText) != 0) {
                return false;
            }
            first = second;
            second = totalText;
            start += static_cast<int>(totalText.size());
        }
        return true;
    }

public:
    bool isAdditiveNumber(std::string num) {
        for (int firstEnd = 1; firstEnd < static_cast<int>(num.size()); firstEnd++) {
            for (int secondEnd = firstEnd + 1; secondEnd < static_cast<int>(num.size()); secondEnd++) {
                if (valid(num, num.substr(0, firstEnd), num.substr(firstEnd, secondEnd - firstEnd), secondEnd)) {
                    return true;
                }
            }
        }
        return false;
    }
};
