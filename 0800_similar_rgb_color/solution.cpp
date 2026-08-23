// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

#include <cstdio>
#include <string>

class Solution {
public:
    std::string similarRGB(std::string color) {
        auto closest = [](const std::string& component) -> std::string {
            int value = std::stoi(component, nullptr, 16);
            int rounded = (value + 8) / 17;
            char buf[3];
            std::snprintf(buf, sizeof(buf), "%x%x", rounded, rounded);
            return buf;
        };
        return "#" + closest(color.substr(1, 2)) + closest(color.substr(3, 2)) +
               closest(color.substr(5, 2));
    }
};
