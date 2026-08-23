// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> addOperators(const std::string& num, int target) {
        std::vector<std::string> result;

        auto backtrack = [&](auto&& self, int index, std::string path, long long value,
                             long long previous) -> void {
            if (index == static_cast<int>(num.size())) {
                if (value == target) {
                    result.push_back(path);
                }
                return;
            }
            for (int end = index; end < static_cast<int>(num.size()); end++) {
                if (end > index && num[index] == '0') {
                    break;
                }
                std::string currentStr = num.substr(index, end - index + 1);
                long long current = std::stoll(currentStr);
                if (index == 0) {
                    self(self, end + 1, currentStr, current, current);
                } else {
                    self(self, end + 1, path + "+" + currentStr, value + current, current);
                    self(self, end + 1, path + "-" + currentStr, value - current, -current);
                    self(self, end + 1, path + "*" + currentStr,
                         value - previous + previous * current, previous * current);
                }
            }
        };

        backtrack(backtrack, 0, "", 0, 0);
        return result;
    }
};
