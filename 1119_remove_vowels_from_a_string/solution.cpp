// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

#include <string>

class Solution {
public:
    std::string removeVowels(std::string s) {
        std::string ans;
        for (char ch : s) {
            if (ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u') {
                ans.push_back(ch);
            }
        }
        return ans;
    }
};
