// LeetCode 0179 - Largest Number
// https://leetcode.com/problems/largest-number/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string largestNumber(std::vector<int>& nums) {
        std::vector<std::string> parts;
        for (int num : nums) {
            parts.push_back(std::to_string(num));
        }
        std::sort(parts.begin(), parts.end(), [](const std::string& a, const std::string& b) {
            return a + b > b + a;
        });
        if (parts[0] == "0") {
            return "0";
        }

        std::string result;
        for (const std::string& part : parts) {
            result += part;
        }
        return result;
    }
};