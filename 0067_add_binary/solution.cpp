// LeetCode 0067 - Add Binary
// https://leetcode.com/problems/add-binary/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string addBinary(std::string a, std::string b) {
        int i = static_cast<int>(a.size()) - 1;
        int j = static_cast<int>(b.size()) - 1;
        int carry = 0;
        std::string result;

        while (i >= 0 || j >= 0 || carry) {
            int total = carry;
            if (i >= 0) {
                total += a[i] - '0';
                --i;
            }
            if (j >= 0) {
                total += b[j] - '0';
                --j;
            }
            result.push_back(static_cast<char>('0' + (total % 2)));
            carry = total / 2;
        }

        std::reverse(result.begin(), result.end());
        return result;
    }
};
