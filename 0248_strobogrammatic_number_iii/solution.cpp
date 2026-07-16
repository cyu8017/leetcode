// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

#include <string>
#include <vector>

class Solution {
public:
    int strobogrammaticInRange(std::string low, std::string high) {
        long long lowValue = std::stoll(low);
        long long highValue = std::stoll(high);
        int count = 0;

        for (int length = static_cast<int>(low.size()); length <= static_cast<int>(high.size()); length++) {
            for (const std::string& value : build(0, length - 1)) {
                long long numeric = std::stoll(value);
                if (lowValue <= numeric && numeric <= highValue) {
                    count++;
                }
            }
        }
        return count;
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
