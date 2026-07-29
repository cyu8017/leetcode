// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

#include <string>
#include <vector>

class Solution {
public:
    int maximumSwap(int num) {
        std::string digits = std::to_string(num);
        std::vector<int> last(10, -1);
        for (int i = 0; i < static_cast<int>(digits.size()); ++i) {
            last[digits[i] - '0'] = i;
        }
        for (int i = 0; i < static_cast<int>(digits.size()); ++i) {
            for (int candidate = 9; candidate > digits[i] - '0'; --candidate) {
                if (last[candidate] > i) {
                    std::swap(digits[i], digits[last[candidate]]);
                    return std::stoi(digits);
                }
            }
        }
        return num;
    }
};
