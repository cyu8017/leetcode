// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

#include <string>
#include <unordered_map>

class Solution {
public:
    bool confusingNumber(int n) {
        static const std::unordered_map<char, char> rotate = {
            {'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};
        std::string s = std::to_string(n);
        std::string rotated;
        rotated.reserve(s.size());
        for (int i = static_cast<int>(s.size()) - 1; i >= 0; --i) {
            auto it = rotate.find(s[i]);
            if (it == rotate.end()) {
                return false;
            }
            rotated.push_back(it->second);
        }
        return rotated != s;
    }
};
