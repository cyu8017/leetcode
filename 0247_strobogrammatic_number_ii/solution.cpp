// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> findStrobogrammatic(int n) {
        return build(0, n - 1);
    }

private:
    static const std::vector<std::pair<std::string, std::string>> pairs;

    std::vector<std::string> build(int left, int right) {
        if (left > right) {
            return {""};
        }
        if (left == right) {
            return {"0", "1", "8"};
        }

        std::vector<std::string> result;
        for (const auto& [start, end] : pairs) {
            if (left == 0 && start == "0") {
                continue;
            }
            for (const std::string& middle : build(left + 1, right - 1)) {
                result.push_back(start + middle + end);
            }
        }
        return result;
    }
};

const std::vector<std::pair<std::string, std::string>> Solution::pairs = {
    {"0", "0"},
    {"1", "1"},
    {"6", "9"},
    {"8", "8"},
    {"9", "6"},
};
