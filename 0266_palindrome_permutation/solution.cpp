// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

#include <string>
using namespace std;

class Solution {
public:
    bool canPermutePalindrome(string s) {
        int counts[26] = {0};
        for (char ch : s) {
            counts[ch - 'a']++;
        }
        int odd = 0;
        for (int count : counts) {
            if (count % 2 != 0) {
                odd++;
            }
        }
        return odd <= 1;
    }
};
