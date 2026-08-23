// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string sortVowels(std::string s) {
        auto isVowel = [](char c) {
            return c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||
                   c=='A'||c=='E'||c=='I'||c=='O'||c=='U';
        };
        std::string vowels;
        for (char c : s) if (isVowel(c)) vowels.push_back(c);
        std::sort(vowels.begin(), vowels.end());
        int vi = 0;
        for (char& c : s) if (isVowel(c)) c = vowels[vi++];
        return s;
    }
};
