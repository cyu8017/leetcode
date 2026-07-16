// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

#include <string>
#include <vector>

class Solution {
public:
    std::string multiply(std::string num1, std::string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }

        int m = static_cast<int>(num1.size());
        int n = static_cast<int>(num2.size());
        std::vector<int> positions(m + n, 0);

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int product = (num1[i] - '0') * (num2[j] - '0');
                int low = i + j + 1;
                int high = i + j;
                int total = product + positions[low];
                positions[low] = total % 10;
                positions[high] += total / 10;
            }
        }

        std::string result;
        result.reserve(positions.size());
        for (int digit : positions) {
            result.push_back(static_cast<char>('0' + digit));
        }

        size_t start = result.find_first_not_of('0');
        if (start == std::string::npos) {
            return "0";
        }
        return result.substr(start);
    }
};
