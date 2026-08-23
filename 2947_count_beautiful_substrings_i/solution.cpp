// LeetCode 2947 - Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/

#include <string>

class Solution {
public:
    int beautifulSubstrings(std::string s, int k) {
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        int ans = 0, n = (int)s.size();
        for (int i = 0; i < n; i++) {
            int v = 0, c = 0;
            for (int j = i; j < n; j++) {
                if (isVowel(s[j])) v++;
                else c++;
                if (v == c && (v * c) % k == 0) ans++;
            }
        }
        return ans;
    }
};
