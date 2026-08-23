// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

#include <string>
#include <unordered_map>

class Solution {
public:
    bool isStrobogrammatic(std::string num) {
        std::unordered_map<char, char> mapping = {
            {'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}
        };
        int left = 0;
        int right = static_cast<int>(num.size()) - 1;
        while (left <= right) {
            if (mapping[num[left]] != num[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
