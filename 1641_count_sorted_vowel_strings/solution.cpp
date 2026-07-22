// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution {
public:
    int countVowelStrings(int n) {
        // C(n+4, 4)
        long long ans = 1;
        for (int i = 1; i <= 4; ++i) {
            ans = ans * (n + 4 - i + 1) / i;
        }
        return static_cast<int>(ans);
    }
};
