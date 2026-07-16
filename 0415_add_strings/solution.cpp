// LeetCode 0415 - Add Strings
// https://leetcode.com/problems/add-strings/

#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    string addStrings(string num1, string num2) {
        int index1 = (int)num1.size() - 1;
        int index2 = (int)num2.size() - 1;
        int carry = 0;
        string digits;

        while (index1 >= 0 || index2 >= 0 || carry) {
            if (index1 >= 0) {
                carry += num1[index1] - '0';
                --index1;
            }
            if (index2 >= 0) {
                carry += num2[index2] - '0';
                --index2;
            }
            digits.push_back(static_cast<char>('0' + carry % 10));
            carry /= 10;
        }

        reverse(digits.begin(), digits.end());
        return digits;
    }
};
